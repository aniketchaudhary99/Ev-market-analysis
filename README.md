<div align="center">

# EV Atlas
### Electric Vehicle Market Performance & Insights

[Tableau Dashboard](https://public.tableau.com/views/EvMarketAnalysisDashboard/Dashboard1) · [Development Report](docs/PROJECT_DOCUMENTATION.md) · [Upload & Deployment Guide](UPLOAD_STEPS.md)

**199,999 cleaned training records · 200 manufacturers · 15 vehicle categories**

</div>

## About the project

This project explores a supplied electric-vehicle dataset using Python, SQLite, Tableau Public, Flask and Plotly. It compares vehicle categories, manufacturer portfolios, battery technologies, manufacturing countries, pricing and driving range.

The Tableau dashboard is published. The website includes an overview with six interactive previews, a dashboard embed and a methodology page. Its blue EV Atlas theme is designed for desktop and mobile widths.

**Dashboard:** [Open EV Market Analysis in Tableau Public](https://public.tableau.com/views/EvMarketAnalysisDashboard/Dashboard1)

**Expected website address after deployment:** [aniketchaudhary99.github.io/Ev-market-analysis](https://aniketchaudhary99.github.io/Ev-market-analysis/)

A separate Story URL was not supplied, so the website does not show a Story navigation link. Set `TABLEAU_STORY_URL` after publishing one to enable it.

## Data and scope

The supplied source files have 200,000 training rows and 100,000 test rows, each with 37 columns. The preparation script removes one duplicate training identifier and builds dashboard summaries from **199,999 cleaned training records**. The test records remain in a separate table and are excluded from those summaries.

The CSVs are included as **lossless `.csv.gz` files**. The build script reads them directly; no manual extraction is needed. The files describe vehicles and do not include customer contact information.

Missing numeric values use training-set medians, except missing annual sales values, which become zero. Missing categorical values become `Unknown`. The scripts also trim text, convert numeric types and constrain non-negative measures and rating ranges.

These are supplied project records, not independently verified official market statistics. In particular, summed `annual_sales_units` should not be presented as verified worldwide or country sales totals.

## Website and visualizations

The web overview contains six Plotly previews:

- Vehicle records by category
- Top manufacturers by vehicle-record count
- Battery technology distribution
- Records by model year
- Records by manufacturing country
- Average price versus range by category

The Tableau build guide describes nine worksheet designs, calculated fields, filters and an eight-scene storyboard. The published workbook should be checked separately against that guide; the presence of a specification is not evidence that every view or calculation has been completed.

## Run locally

Python 3.10 or later is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` in PowerShell. Open `http://127.0.0.1:5000` after starting Flask. The supplied aggregate files are enough to display the website; the dashboard embed needs an internet connection.

To rebuild the SQLite database and summaries:

```bash
python src/build_data.py
python src/validate_project.py
```

To export a clean CSV for Tableau:

```bash
python src/export_clean_csv.py
```

The SQLite database, local environment and clean CSV export are ignored by Git.

## Publish with GitHub Pages

Upload the extracted repository files, including `.github/workflows/pages.yml`, to the `main` branch of [this repository](https://github.com/aniketchaudhary99/Ev-market-analysis). In **Settings → Pages**, choose **GitHub Actions** as the source. See [UPLOAD_STEPS.md](UPLOAD_STEPS.md) for the full upload procedure.

The workflow installs the web dependencies, runs `src/export_site.py`, and publishes `dist/`. Further pushes to `main` trigger deployment automatically. The build uses the existing aggregate files; it does not rebuild the source database.

GitHub Pages serves generated HTML, CSS and chart previews. Tableau hosts the embedded dashboard. Flask and SQLite remain available for local use.

## Repository guide

| Path | Purpose |
|---|---|
| `app.py`, `templates/`, `static/` | Flask application and website styling |
| `src/build_data.py` | Data cleaning, SQLite storage, aggregates and query timings |
| `src/export_site.py` | Static website export for GitHub Pages |
| `src/export_clean_csv.py` | Clean CSV export for Tableau |
| `src/validate_project.py` | Data and aggregate validation checks |
| `data/` | Compressed source CSVs |
| `sql/` | Database schema and analysis queries |
| `outputs/` | Prepared summaries and supplied validation reports |
| `docs/PROJECT_DOCUMENTATION.md` | Detailed development report |
| `docs/TABLEAU_BUILD_GUIDE.md` | Tableau worksheet and Story specifications |
| `docs/performance_test.md` | Tableau performance recording template |
| `.github/workflows/pages.yml` | Automatic Pages deployment |

## Current limits

Local SQL timings are included in `outputs/`; they are distinct from Tableau loading and filter timings. The latter, mobile workbook layouts, Story publication and the explanation video must be confirmed separately. Existing report files record earlier runs and should not be described as measurements from this deployment build.

The dashboard URL contains only a public Tableau view address. Authentication files, `.env`, virtual environments and operating-system files are excluded from the upload package.
