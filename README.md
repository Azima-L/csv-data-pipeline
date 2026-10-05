# CSV Data Pipeline

A modular, command-line ETL pipeline that profiles, validates, and transforms CSV datasets using Python and pandas. Built with configurable validation rules, structured audit reporting, and a tested core logic layer.

</br>

---

## Pipeline Stages

- `profile.py`   — explores and summarises the dataset
- `validator.py` — identifies data quality issues
- `transform.py` — cleans and normalises the data
- `report.py`    — generates a structured audit report (.txt file)
- `main.py`      — orchestrates the full pipeline, CLI entry point

</br>

---

## Features

- **Config-driven validation** — define salary range, name format, and date format rules in `config/rules.json` without touching code
- **Three validation checks** — name casing, salary range, and date format with per-record issue reporting
- **Automated audit reports** — timestamped `.txt` reports written to `reports/` after every pipeline run
- **Modular architecture** — pure logic in `core.py`, UI concerns in `validator.py`, orchestration in `main.py`
- **Tested core logic** — 13 pytest unit tests covering all validation functions and boundary cases
- **CLI support** — configurable input, output, and config paths via argparse flags

</br>

---

## Project Structure

```text
csv-data-pipeline/
├── config/
│   └── rules.json          # validation rules config
├── data/
│   └── employees.csv       # raw input dataset
├── reports/                # generated audit reports (gitignored)
├── src/
│   ├── __init__.py
│   ├── core.py             # pure validation logic
│   ├── profile.py          # data profiling and exploration
│   ├── validator.py        # DataFrame-level validation
│   ├── transform.py        # data cleaning and normalisation
│   ├── report.py           # audit report generation
│   └── main.py             # pipeline entry point
├── tests/
│   ├── __init__.py
│   └── test_validator.py   # pytest unit tests
├── conftest.py             # project root runner (empty)
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

</br>

---

## Requirements

- Python 3.10+
- pandas
- pytest

```bash
pip install -r requirements.txt
```

</br>

---

## Usage

Run the full pipeline with defaults:

```bash
python src/main.py
```

Run with custom files:

```bash
python src/main.py --input your_data.csv --output your_data_clean.csv --config rules.json
```

Run individual stages:

```bash
python src/profile.py
python src/validator.py
```

Run the test suite:

```bash
pytest tests/ -v
```

</br>

---

## Configuration

Validation rules are defined in `config/rules.json`:

```json
{
    "salary_min": 50000,
    "salary_max": 200000,
    "name_format": "title_case",
    "date_format": "YYYY-MM-DD"
}
```

Supported name formats (currently): `title_case`, `upper_case`, `lower_case`

</br>

---

## My Roadmap (For this project)

- [x] v0.1.0 — ETL pipeline: profile, validate, transform
- [x] v0.2.0 — main.py orchestration, argparse CLI
- [x] v0.3.0 — repo restructure, requirements.txt
- [x] v0.4.0 — audit report with issue details and timestamp
- [x] v0.5.0 — JSON config for configurable validation rules
- [x] v0.6.0 — pytest suite: 13 passing tests
- [..] v1.0.0 — FastAPI layer, real Kaggle dataset, Docker

</br>

---

## License

Distributed under the MIT License. See `LICENSE` for details.