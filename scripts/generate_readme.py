#!/usr/bin/env python3
"""Regenerate the template catalog section of README.md from templates/*.yaml.

    python3 scripts/generate_readme.py            # rewrite README.md in place
    python3 scripts/generate_readme.py --check    # exit 1 if README is stale

Only the blocks between the BEGIN/END markers are owned by this script:

    <!-- BEGIN TEMPLATE TOC -->    ... <!-- END TEMPLATE TOC -->
    <!-- BEGIN TEMPLATE CATALOG --> ... <!-- END TEMPLATE CATALOG -->

Everything outside the markers is hand-written — edit it freely. Templates are
grouped by their FIRST category (the primary one), so each app appears exactly
once. Requires PyYAML, same as generate_index.py.
"""
import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - contributor ergonomics
    sys.exit("PyYAML is required to regenerate the README: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"
README = ROOT / "README.md"

SITE = "https://serverkit.ai/templates"

TOC_BEGIN = "<!-- BEGIN TEMPLATE TOC -->"
TOC_END = "<!-- END TEMPLATE TOC -->"
CAT_BEGIN = "<!-- BEGIN TEMPLATE CATALOG -->"
CAT_END = "<!-- END TEMPLATE CATALOG -->"

# Section order, emoji, and display titles for primary categories. Categories
# not listed here still render — appended alphabetically with a generic icon —
# so a new category never breaks the build.
SECTIONS = [
    ("ai",              "🤖", "AI & LLM"),
    ("analytics",       "📊", "Analytics"),
    ("business",        "💼", "Business & ERP"),
    ("cms",             "📝", "CMS & Websites"),
    ("collaboration",   "🤝", "Collaboration & Chat"),
    ("community",       "👥", "Community & Forums"),
    ("database",        "🗄️", "Databases"),
    ("development",     "🛠️", "Development"),
    ("devops",          "⚙️", "DevOps & Containers"),
    ("documents",       "📄", "Documents & E-Signing"),
    ("finance",         "💰", "Finance"),
    ("gaming",          "🎮", "Gaming"),
    ("home-automation", "🏠", "Home Automation"),
    ("media",           "🎬", "Media & Downloads"),
    ("monitoring",      "📈", "Monitoring & Status"),
    ("networking",      "🌐", "Networking & DNS"),
    ("news",            "📰", "News & RSS"),
    ("notes",           "🗒️", "Notes & Wikis"),
    ("notifications",   "🔔", "Notifications"),
    ("productivity",    "✅", "Productivity"),
    ("search",          "🔍", "Search"),
    ("security",        "🔒", "Security & Auth"),
    ("storage",         "💾", "Storage & Files"),
]


def anchor(emoji_title: str) -> str:
    """GitHub heading anchor: lowercase, spaces to hyphens, strip most
    punctuation, keep unicode (emoji survive as-is in GitHub's algorithm but
    contribute a leading hyphen via the space after them)."""
    text = emoji_title.lower()
    out = []
    for ch in text:
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "-"):
            out.append("-")
        # everything else (®, &, emoji) is dropped by GitHub's slugger
    return "".join(out)


def esc(text: str) -> str:
    return str(text or "").replace("|", "\\|").strip()


def load_templates():
    groups = {}
    for path in sorted(TEMPLATES_DIR.glob("*.y*ml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        tid = doc.get("id") or path.stem
        cats = doc.get("categories") or ["other"]
        primary = cats[0]
        groups.setdefault(primary, []).append({
            "id": tid,
            "name": doc.get("name", tid),
            "description": doc.get("description", ""),
            "website": doc.get("website"),
            "kind": doc.get("kind", "compose"),
        })
    for entries in groups.values():
        entries.sort(key=lambda e: e["name"].lower())
    return groups


def render(groups):
    known = [key for key, _, _ in SECTIONS]
    ordered = [(key, emoji, title) for key, emoji, title in SECTIONS if key in groups]
    for key in sorted(groups):
        if key not in known:
            ordered.append((key, "📦", key.replace("-", " ").title()))

    total = sum(len(v) for v in groups.values())

    toc_lines = []
    for key, emoji, title in ordered:
        heading = f"{emoji} {title}"
        toc_lines.append(f"- [{heading}](#{anchor(heading)}) — {len(groups[key])}")
    toc = "\n".join(toc_lines)

    cat_lines = [f"**{total} templates** and counting — grouped by primary category.\n"]
    for key, emoji, title in ordered:
        cat_lines.append(f"### {emoji} {title}\n")
        cat_lines.append("| App | Description | Links |")
        cat_lines.append("|---|---|---|")
        for e in groups[key]:
            name = esc(e["name"])
            app = f"[{name}]({e['website']})" if e.get("website") else name
            badge = " 🚀" if e["kind"] == "repo" else ""
            links = (f"[Install]({SITE}/{e['id']}) · "
                     f"[YAML](templates/{e['id']}.yaml)")
            cat_lines.append(f"| **{app}**{badge} | {esc(e['description'])} | {links} |")
        cat_lines.append("")
    cat_lines.append("🚀 = deployed straight from its Git repository (repo template) "
                     "rather than a Docker Compose stack.")
    catalog = "\n".join(cat_lines)

    return toc, catalog


def splice(text: str, begin: str, end: str, payload: str) -> str:
    try:
        head, rest = text.split(begin, 1)
        _, tail = rest.split(end, 1)
    except ValueError:
        sys.exit(f"README.md is missing the {begin} / {end} markers")
    return f"{head}{begin}\n{payload}\n{end}{tail}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify README.md matches templates/ without writing")
    args = parser.parse_args()

    toc, catalog = render(load_templates())
    current = README.read_text(encoding="utf-8")
    fresh = splice(current, TOC_BEGIN, TOC_END, toc)
    fresh = splice(fresh, CAT_BEGIN, CAT_END, catalog)

    if args.check:
        if fresh != current:
            print("README.md catalog is stale — run: python3 scripts/generate_readme.py")
            return 1
        print("README.md catalog is up to date")
        return 0

    README.write_text(fresh, encoding="utf-8", newline="\n")
    print(f"wrote README.md catalog ({sum(len(v) for v in load_templates().values())} templates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
