"""Offline WordPress runtime regressions; optional full core-template parity.

Source: jhd3197/ServerKit@10b5383ae3f926ee7cfb100f17cbb553723f64ca
Run: python scripts/test_wordpress.py
Set SERVERKIT_CORE_TEMPLATES_DIR to a core backend/templates directory to
also check full parsed-template parity (used by registry CI).
"""
import hashlib
import json
import os
from pathlib import Path
import unittest

import yaml

from compose_check import ROOT, render


IDS = ("wordpress", "wordpress-external-db")


class WordPressTests(unittest.TestCase):
    def setUp(self):
        self.templates = {
            tid: yaml.safe_load((ROOT / "templates" / f"{tid}.yaml").read_text(encoding="utf-8"))
            for tid in IDS
        }

    def test_runtime_protections_survive_rendering(self):
        for tid, template in self.templates.items():
            with self.subTest(template=tid):
                text, values, files = render(template, "wp-regression", [18300])
                service = yaml.safe_load(text)["services"]["wordpress"]
                self.assertEqual(service["image"], "serverkit-wp-runtime:wp-regression")
                self.assertEqual(service["build"], {
                    "context": ".", "dockerfile": "Dockerfile.serverkit-php"})
                dockerfile = dict(files)[service["build"]["dockerfile"]]
                self.assertIn("FROM wordpress:" + values["VERSION"], dockerfile)
                self.assertNotIn("${", dockerfile)
                # Requirements copied from the official core source above.
                self.assertIn('$min=["8.2"=>"8.2.35","8.3"=>"8.3.36"]', dockerfile)
                self.assertIn('exit(isset($min[$v]) && version_compare(PHP_VERSION,$min[$v],">=") ? 0 : 1)', dockerfile)
                self.assertIn("&& docker-php-ext-install pdo_mysql", dockerfile)
                self.assertIn("session.upload_progress.enabled=0", dockerfile)
                self.assertIn("/usr/local/etc/php/conf.d/zz-serverkit-security.ini", dockerfile)
                self.assertIn("php_admin_flag session.upload_progress.enabled Off", dockerfile)
                self.assertIn("/etc/apache2/conf-available/serverkit-php-security.conf", dockerfile)
                self.assertIn("&& a2enconf serverkit-php-security", dockerfile)

    def test_database_variants(self):
        bundled = self.templates["wordpress"]["compose"]
        self.assertEqual(set(bundled["services"]), {"wordpress", "db", "redis"})
        self.assertEqual(set(bundled["services"]["wordpress"]["depends_on"]), {"db", "redis"})
        self.assertIn("WORDPRESS_DB_HOST=db", bundled["services"]["wordpress"]["environment"])
        self.assertIn("MYSQL_PASSWORD=${WP_DB_PASSWORD}", bundled["services"]["db"]["environment"])
        external = self.templates["wordpress-external-db"]["compose"]
        self.assertEqual(set(external["services"]), {"wordpress"})
        self.assertEqual(set(external["volumes"]), {"wordpress_html"})
        service = external["services"]["wordpress"]
        self.assertNotIn("depends_on", service)
        self.assertEqual(set(service["environment"]), {
            "WORDPRESS_DB_HOST=${DB_HOST}:${DB_PORT}",
            "WORDPRESS_DB_USER=${DB_USER}",
            "WORDPRESS_DB_PASSWORD=${DB_PASSWORD}",
            "WORDPRESS_DB_NAME=${DB_NAME}",
            "WORDPRESS_TABLE_PREFIX=${TABLE_PREFIX}",
        })

    def test_variants_share_runtime(self):
        first, second = (self.templates[tid] for tid in IDS)
        self.assertEqual(first["files"], second["files"])
        self.assertEqual(first["version"], second["version"])
        self.assertEqual(first["variables"][0], second["variables"][0])

    def test_catalog_metadata_and_hashes(self):
        entries = {entry["id"]: entry for entry in json.loads(
            (ROOT / "index.json").read_text(encoding="utf-8"))["templates"]}
        for tid, template in self.templates.items():
            with self.subTest(template=tid):
                self.assertEqual(entries[tid]["version"], template["version"])
                self.assertEqual(entries[tid]["sha256"], hashlib.sha256(
                    (ROOT / "templates" / f"{tid}.yaml").read_bytes()).hexdigest())

    @unittest.skipUnless(os.environ.get("SERVERKIT_CORE_TEMPLATES_DIR"),
                         "Set SERVERKIT_CORE_TEMPLATES_DIR for official core parity")
    def test_core_parity(self):
        for tid, template in self.templates.items():
            with self.subTest(template=tid):
                source = Path(os.environ["SERVERKIT_CORE_TEMPLATES_DIR"]) / f"{tid}.yaml"
                self.assertEqual(template, yaml.safe_load(source.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
