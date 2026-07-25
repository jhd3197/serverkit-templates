# Releasing

There is no build and no release artifact. Panels read `index.json` and
`templates/*.yaml` **straight from the default branch**, so *merging to `main`
is publishing*. A bad merge reaches every connected panel on its next catalog
load.

## Checklist

```bash
python3 scripts/generate_index.py        # rebuild the catalog
python3 scripts/validate.py              # must exit 0
git diff --stat                          # sanity-check what moved
```

`validate.py` exits non-zero on a stale index, a missing or orphaned template
file, a duplicate id, or a sha256 that no longer matches the bytes on disk.
Never hand-edit `index.json` — regenerate it, or the hashes drift and the
validator will say so.

## What panels see, and when

| Change | Effect |
|---|---|
| New `templates/<id>.yaml` + reindex | appears in the catalog |
| Edited template, `version` bumped | installed apps show "update available" |
| Edited template, `version` unchanged | new installs get the fix; existing apps are not prompted |
| Removed template | disappears from the catalog; already-installed apps keep running |

Removing a template does **not** uninstall anything — an installed app owns its
generated `docker-compose.yml`. But `check_updates()` can no longer resolve the
template, so prefer leaving it in place unless it is actively harmful.

## Caching

Panels fetch this repo over the network on catalog load. If it is proxied
through `serverkit.ai`, that proxy caches with a TTL and serves the last-good
copy when upstream fails — so a merge can take a few minutes to appear
everywhere. Raw `raw.githubusercontent.com` URLs have their own CDN caching with
similar delay. Neither is instant; do not treat a merge as immediately live.

## Rollback

`git revert` the merge and rerun `generate_index.py`. There are no version tags
to unpublish and nothing to yank — the branch tip *is* the published state.

## Breaking the contract

`index.json`'s shape is fixed by the panel's
`TemplateService.fetch_remote_templates()` / `get_template()`, which build
`<repo_url>/index.json` and `<repo_url>/templates/<id>.yaml`. Older panels will
keep reading this branch forever, so:

- **Additive only.** New optional fields are fine; unknown fields are ignored.
- Renaming or removing a field, or changing `schema_version`, strands every
  panel that has not upgraded. Ship a parallel path instead.
