#!/usr/bin/env python3
"""Validate index.json and the templates/ tree against the registry rules.

Dependency-free on purpose so a contributor (or CI) can check a PR with any
Python 3 and no install:

    python3 scripts/validate.py

Exit 0 = valid (warnings allowed), exit 1 = errors. The rules mirror
schema/index.schema.json plus the cross-file checks a JSON Schema cannot
express: every entry has a real templates/<id>.yaml, every file has an entry,
ids are unique and match their filename, and each sha256 matches the bytes on
disk.

Deliberately does NOT parse the template YAML (that would need PyYAML). Deep
template validation lives in the panel — backend/tests/test_template_catalog_
validation.py certifies the bundled catalog against TemplateService.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

# Windows consoles often default to cp1252, which can't print the check marks;
# never let the report itself crash the validator.
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / 'index.json'
TEMPLATES_DIR = ROOT / 'templates'

SLUG_RE = re.compile(r'^[a-z0-9][a-z0-9-]*$')
SHA256_RE = re.compile(r'^[a-f0-9]{64}$')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
ICON_RE = re.compile(r'^(https://|data:image/)')

KNOWN_TOP = {'name', 'schema_version', 'updated', 'count', 'templates'}
KNOWN_ENTRY = {'id', 'name', 'version', 'revision', 'description', 'icon',
               'categories', 'sha256'}

errors: list[str] = []
warnings: list[str] = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not INDEX.exists():
        print('✘ index.json not found')
        return 1
    try:
        index = json.loads(INDEX.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        print(f'✘ index.json is not valid JSON: {exc}')
        return 1

    # ---- document level -------------------------------------------------
    for field in ('name', 'schema_version', 'templates'):
        if field not in index:
            err(f'index.json is missing required field {field!r}')
    if index.get('schema_version') not in (1, None):
        err(f'unsupported schema_version {index.get("schema_version")!r} (expected 1)')
    if 'updated' in index and not DATE_RE.match(str(index['updated'])):
        err(f'updated {index["updated"]!r} is not YYYY-MM-DD')
    for extra in sorted(set(index) - KNOWN_TOP):
        warn(f'unknown top-level field {extra!r}')

    entries = index.get('templates') or []
    if not isinstance(entries, list):
        print('✘ templates must be an array')
        return 1
    if 'count' in index and index['count'] != len(entries):
        err(f'count says {index["count"]} but there are {len(entries)} entries')

    # ---- entry level ----------------------------------------------------
    seen = {}
    for i, entry in enumerate(entries):
        where = f'templates[{i}]'
        if not isinstance(entry, dict):
            err(f'{where} is not an object')
            continue
        tid = entry.get('id')
        if not tid:
            err(f'{where} has no id')
            continue
        where = f'{tid}'
        if not SLUG_RE.match(tid):
            err(f'{where}: id is not a lowercase slug')
        if tid in seen:
            err(f'{where}: duplicate id (also at index {seen[tid]})')
        seen[tid] = i

        if not entry.get('name'):
            warn(f'{where}: no name — the catalog card will fall back to the id')
        if not entry.get('description'):
            warn(f'{where}: no description')
        if not entry.get('categories'):
            warn(f'{where}: no categories — it will not appear under any filter')
        for cat in entry.get('categories') or []:
            if not SLUG_RE.match(str(cat)):
                err(f'{where}: category {cat!r} is not a lowercase slug')
        icon = entry.get('icon')
        if icon is not None and not ICON_RE.match(str(icon)):
            err(f'{where}: icon must be an https:// URL or a data:image/ URI')
        rev = entry.get('revision')
        if rev is not None and (not isinstance(rev, int) or rev < 1):
            err(f'{where}: revision must be an integer >= 1')
        for extra in sorted(set(entry) - KNOWN_ENTRY):
            warn(f'{where}: unknown field {extra!r}')

        # ---- cross-file: the artifact the panel will actually download ---
        path = TEMPLATES_DIR / f'{tid}.yaml'
        if not path.exists():
            alt = TEMPLATES_DIR / f'{tid}.yml'
            if alt.exists():
                err(f'{where}: file is {alt.name}, but the panel fetches templates/{tid}.yaml')
            else:
                err(f'{where}: listed in the index but templates/{tid}.yaml is missing')
            continue
        declared = entry.get('sha256')
        if declared is None:
            warn(f'{where}: no sha256 — run scripts/generate_index.py')
        elif not SHA256_RE.match(str(declared)):
            err(f'{where}: sha256 is not 64 lowercase hex chars')
        elif declared != sha256_of(path):
            err(f'{where}: sha256 does not match templates/{tid}.yaml — index is stale, '
                f'run scripts/generate_index.py')

    # ---- cross-file: files with no entry --------------------------------
    for path in sorted(TEMPLATES_DIR.glob('*.y*ml')):
        if path.stem not in seen:
            err(f'templates/{path.name} exists but is not listed in index.json — '
                f'run scripts/generate_index.py')

    # ---- report ---------------------------------------------------------
    for msg in warnings:
        print(f'⚠ {msg}')
    for msg in errors:
        print(f'✘ {msg}')
    if errors:
        print(f'\n✘ {len(errors)} error(s), {len(warnings)} warning(s)')
        return 1
    print(f'✔ {len(entries)} templates valid ({len(warnings)} warning(s))')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
