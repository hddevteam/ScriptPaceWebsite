# 稿随 / ScriptPace Website

Marketing, product support, privacy, and terms website for 稿随 / ScriptPace.

The site is plain static HTML, CSS, and JavaScript and is designed for GitHub
Pages. Chinese and English content live under separate route trees:

- `/zh-hans/`
- `/en/`

## Local preview

```bash
python3 -m http.server 4173
```

Open <http://127.0.0.1:4173/> in a browser.

## Validation

```bash
node --check site-config.js
python3 scripts/check-site.py
python3 scripts/check-links.py
python3 scripts/check-responsive-assets.py
git diff --check
```

The production checks intentionally fail until the public support email is
entered in `site-config.js`. Do not substitute a guessed address.

## Publishing

`main` is the intended GitHub Pages source branch. The workflow under
`.github/workflows/pages.yml` validates the site before deployment. The remote
repository is still awaiting release integration, so the feature branch may be
the default branch temporarily; do not treat that state as a published site.
A custom domain is not configured until its exact value is explicitly approved.
