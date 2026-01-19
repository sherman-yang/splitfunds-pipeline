# Split Share Funds Pipeline

This repo contains the private pipeline to build a daily snapshot of Canadian split share funds and publish a static site.

## Quick start

```bash
python scripts/refresh.py --output site
```

Generated output:
- `site/index.html`
- `site/assets/app.css`
- `site/assets/app.js`
- `site/data/latest.json`
- `site/data/latest.csv`

Configuration and sample data live under `config/` and `data/source/`.

For full setup (GitHub Actions + public site repo), see `SETUP.md`.
