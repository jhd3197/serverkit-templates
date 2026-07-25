# ServerKit Templates

The official one-click app template registry for [ServerKit](https://github.com/jhd3197/ServerKit).

A template is a small YAML file describing how to run an application — a Docker
Compose stack, the variables to ask for, ports, volumes, and any post-install
steps. Adding one here publishes it to every panel **without a ServerKit
release**.

## How a panel consumes this repo

The contract is two files on any static host:

```
<repo_url>/index.json              ← the catalog
<repo_url>/templates/<id>.yaml     ← fetched on demand, when opened or installed
```

The panel lists `index.json` alongside its bundled templates, and only downloads
the full YAML when someone opens or installs one. `<id>` comes straight from the
index entry, so **`id` must equal the filename stem**.

Point a panel at this repo under *Templates → Repositories*, or via the API:

```bash
curl -X POST https://your-panel/api/v1/templates/repos \
  -H 'Authorization: Bearer <token>' \
  -d '{"name":"serverkit-official",
       "url":"https://raw.githubusercontent.com/jhd3197/serverkit-templates/main"}'
```

## Bundled vs registry

ServerKit **ships these same templates inside the panel**. This repo is not a
replacement for that bundle — it is the layer on top:

| | Bundled in the panel | This registry |
|---|---|---|
| Works offline / air-gapped | yes | no |
| Available on a fresh install | yes | needs network |
| Updated without a panel release | no | **yes** |
| Community submissions | no | **yes** |

So the bundle is the known-good floor and stays useful when this repo (or
GitHub) is unreachable; the registry is where new templates land and where fixes
ship between releases.

## Adding a template

1. Write `templates/<id>.yaml`. Copy the closest existing template — that is
   more reliable than any spec, and every file here is a working example.
2. Regenerate and validate:

   ```bash
   python3 scripts/generate_index.py     # needs PyYAML
   python3 scripts/validate.py           # no dependencies
   ```

3. Open a PR. `validate.py` is the review gate.

`id` must be a lowercase slug matching the filename, and the template must
declare at least one of `compose`, `dockerfile` or `ports`. The authoritative
rules live in the panel's `TemplateService.validate_template()` — this repo's
validator deliberately checks only the registry contract (index ↔ files ↔
hashes), not template semantics, so it can stay dependency-free.

## `version` vs `revision`

Two different things, and the distinction matters:

- **`version`** — the version of the *upstream application* (`"1.23"` for Uptime
  Kuma). User-facing.
- **`revision`** — the version of *this template*, for a compose fix, a wrong
  port, or a bad healthcheck that ships no new upstream release.

⚠️ **`revision` is reserved and not yet consumed.** Current panels compare
`version` to decide "update available", so today a template-only fix cannot be
published without also implying an app upgrade. Bump `version` for now; the
field is emitted so the index is ready when panel support lands.

## `sha256`

Every entry carries the SHA-256 of the file the panel will download. Not yet
verified panel-side — it is published so verification can be enabled without
reindexing, and so a PR diff names exactly which templates changed rather than
just showing a churned index.

## Icons

`icon` is an `https://` URL or a `data:image/` URI. Today 63 templates use URLs
(mostly `https://serverkit.ai/imgs/template-icons/…`) and 43 inline an SVG data
URI, which is ~33% of the index by bytes. Workable at this size — the whole
index is 61 KB, 14 KB gzipped — but if the catalog grows substantially, move
icons into an `assets/<id>/` tree like
[serverkit-extensions](https://github.com/jhd3197/serverkit-extensions) does.

## Layout

```
index.json         generated catalog — never hand-edit
templates/         one <id>.yaml per template
schema/            JSON Schema for index.json
scripts/
  generate_index.py  rebuild index.json from templates/ (needs PyYAML)
  validate.py        check the registry contract (no dependencies)
```

See [RELEASING.md](RELEASING.md) for publishing.

## License

MIT — see [LICENSE](LICENSE).
