# Split Share Funds: Setup Guide

This document explains how to configure the private pipeline repo and the public GitHub Pages site.

## 1. Prerequisites

- Python 3.11+
- GitHub account (free)
- Two repos:
  - `splitfunds-pipeline` (private)
  - `splitfunds` (public)

## 2. Repo roles

### Private repo (`splitfunds-pipeline`)
- Runs daily refresh.
- Holds API keys, adapters, validation, scoring logic.
- Generates static site output to `site/`.

### Public repo (`splitfunds`)
- Only stores static output (`index.html`, `assets/`, `data/`).
- Hosts GitHub Pages.

## 3. Local setup (private repo)

```bash
python -m venv .venv
source .venv/bin/activate
python scripts/refresh.py --output site
```

Output files (generated):
- `site/index.html`
- `site/assets/app.css`
- `site/assets/app.js`
- `site/data/latest.json`
- `site/data/latest.csv`
- `data/run_report.json`

## 4. Configure data inputs

### 4.1 Universe and terms
Edit `config/universe.yaml`.

This now defaults to the live TSX directory adapter. You can still add static overrides under `funds` for manual fixes (e.g., `pref_par`, `gate_nav`, `maturity_date`).

### 4.2 Quotes and total return
Live quotes now come from the StockAnalysis watchlist API (configured in `config/sources.yaml`).

The adapter fetches:
- `price`, `volume`, `low52`, `high52`
- `tr1y`, `tr3y`, `tr5y`, `tr10y` (converted to decimal total return)

If you want to revert to local data, switch `quote_adapter` back to `scripts.adapters.local_quotes:load_quotes` and point `paths.quotes` to your JSON file.

Note: StockAnalysis does not return data for every TSX preferred share ticker. Any missing rows will remain null until you add a secondary quotes source.

### 4.3 Issuer NAV and terms updates
Edit `config/issuers.yaml`.

The issuer aggregator scrapes Brompton, Middlefield, and Quadravest pages to collect tickers, distributions, maturity dates, and NAV where available. You can add or remove issuers in this file.

## 5. Adapter model (extensible)

Adapters live in `scripts/adapters/` and are called by `scripts/refresh.py`.

- `tsx_directory.py` pulls the split-share universe from TSX.
- `issuer_aggregate.py` merges issuer scrapes (Brompton, Middlefield, Quadravest).
- `local_quotes.py` still loads quotes from JSON (replace with your API adapter).

To add a new issuer or data provider:
1. Create a new adapter in `scripts/adapters/`.
2. Add it in `config/issuers.yaml` or `config/sources.yaml`.
3. Ensure adapters return the same shape as the local JSON examples.

## 6. Scoring and validation

- Scoring config: `config/scoring.yaml`
- Validation rules: `scripts/validate.py`

Adjust thresholds and weightings in `config/scoring.yaml` to tune risk tolerance.

## 7. GitHub Actions (private repo)

Workflow file: `/.github/workflows/refresh-and-publish.yml`

### Required secrets
- `PUBLIC_REPO_PAT`: fine-grained PAT with write access to the public repo
- `PUBLIC_REPO`: full repo slug for the public site (example: `yourname/splitfunds`)
- `PERF_API_KEY`: only if your adapters need it (store in secrets and read in adapters)

### Configure the public repo target
Set the `PUBLIC_REPO` secret in the private repo to point to your public repo (e.g. `yourname/splitfunds`).

## 8. Public repo setup

Create a new public repo named `splitfunds` and enable Pages.

### Option A: Publish from the default branch (simple)
1. Push generated `site/` contents into the root of the public repo.
2. Enable GitHub Pages from the default branch.

### Option B: Deploy using Actions (recommended)
The pipeline publishes `site/.github/workflows/deploy-pages.yml` into the public repo so you can deploy Pages automatically. If you prefer to add it manually, use this workflow:

```yaml
name: Deploy Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - uses: actions/deploy-pages@v4
```

## 9. Running locally with your own data

1. Update `config/universe.yaml` to your full ticker list.
2. Replace `data/source/quotes.json` and `data/source/issuer_daily.json` with live exports.
3. Run:

```bash
python scripts/refresh.py --output site
```

4. Open `site/index.html` to validate the UI.

## 10. Field reference

All output fields are documented in `splitfunds.md` and are emitted into `site/data/latest.json`.

Key columns:
- `security_type` (`CLASS_A`, `PREFERRED`)
- `discount_to_intrinsic`, `annualized_discount_to_intrinsic`
- `discount_to_par`, `annualized_discount_to_par`
- `years_to_maturity`
- `pref_yield_current`

## 11. Safety notes

- Keep API keys only in the private pipeline repo.
- Never push adapters or raw data that contain credentials to the public repo.
- Only publish `site/` output artifacts.
