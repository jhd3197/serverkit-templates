#!/usr/bin/env python3
"""Regenerate index.json from templates/*.yaml.

    python3 scripts/generate_index.py            # write index.json
    python3 scripts/generate_index.py --check    # exit 1 if index.json is stale

The output shape is fixed by the panel, not by this script: ServerKit's
``TemplateService.fetch_remote_templates()`` fetches ``<repo_url>/index.json``
and reads ``index["templates"]``, then resolves each template on demand from
``<repo_url>/templates/<id>.yaml``. That is the entire contract — a template
repo is just those files on any static host.

Requires PyYAML (``pip install pyyaml``). scripts/validate.py is dependency-free
so contributors can check a PR without installing anything; only regenerating
needs to parse the YAML.
"""
import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - contributor ergonomics
    sys.exit("PyYAML is required to regenerate the index: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"
INDEX = ROOT / "index.json"

SCHEMA_VERSION = 1
REPO_NAME = "serverkit-official"

# Fields copied verbatim from each template into its index entry. The panel
# renders the catalog straight from the index and only downloads the full YAML
# when someone opens or installs a template, so everything the card needs must
# be here — but nothing more, to keep the index small.
CARD_FIELDS = ("name", "version", "description", "icon", "categories", "featured")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_index() -> dict:
    entries = []
    for path in sorted(TEMPLATES_DIR.glob("*.y*ml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        template_id = doc.get("id")
        if not template_id:
            sys.exit(f"{path.name}: template has no 'id'")
        if template_id != path.stem:
            sys.exit(f"{path.name}: id {template_id!r} does not match the filename")

        entry = {"id": template_id}
        for field in CARD_FIELDS:
            value = doc.get(field)
            if value is not None:
                entry[field] = value

        # `revision` is the template's OWN revision, distinct from `version`
        # (which is the upstream application's version, e.g. Uptime Kuma 1.23).
        # Emitted only when a template declares it. Reserved: today's panel
        # compares `version` for update detection, so a template fix cannot yet
        # be shipped without also implying an app upgrade. See README.
        if doc.get("revision") is not None:
            entry["revision"] = doc["revision"]

        # Integrity of the artifact the panel will fetch from templates/<id>.yaml.
        # Not yet verified panel-side; published so verification can be turned on
        # without a reindex, and so a diff shows exactly which templates changed.
        entry["sha256"] = _sha256(path)
        entries.append(entry)

    return {
        "name": REPO_NAME,
        "schema_version": SCHEMA_VERSION,
        "updated": date.today().isoformat(),
        "count": len(entries),
        "templates": entries,
    }


def _comparable(index: dict) -> str:
    """Index minus the date stamp, so --check does not fail merely because a
    day passed without any template changing."""
    return json.dumps({k: v for k, v in index.items() if k != "updated"}, sort_keys=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify index.json matches templates/ without writing")
    args = parser.parse_args()

    fresh = build_index()

    if args.check:
        if not INDEX.exists():
            print("index.json is missing — run: python3 scripts/generate_index.py")
            return 1
        current = json.loads(INDEX.read_text(encoding="utf-8"))
        if _comparable(current) != _comparable(fresh):
            print("index.json is stale — run: python3 scripts/generate_index.py")
            return 1
        print(f"index.json is up to date ({fresh['count']} templates)")
        return 0

    INDEX.write_text(json.dumps(fresh, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {INDEX.relative_to(ROOT)} ({fresh['count']} templates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
