# CSV Data Pipeline

A lightweight ETL pipeline demonstrating data profiling, validation, and transformation using Python and pandas.

This project highlights my learning roadmap to engineer a data workflow from as basic as the foundation level.

---

## Pipeline Stages
- `profile.py`   — explores and summarises the dataset
- `validate.py`  — identifies data quality issues
- `transform.py` — cleans and normalises the data
- `report.py` — generates structured audit report
- `main.py` — orchestrates the full pipeline end to end

---

## Tech Stack
- Python 3.10+
- pandas
- pathlib, argparse, re

---

## System Architecture
```text
csv-data-pipeline/
├── data/
│   └── employees.csv       # my raw dataset
├── src/
│   ├── profile.py          # data exploration and profiling
│   ├── validate.py         # data quality validation
│   ├── transform.py        # data cleaning and normalization
│   ├── report.py           # audit report generation
│   └── main.py             # pipeline orchestration, CLI entry point
├── .gitignore
├── LICENSE                 # MIT licence details
├── README.md               # README file for the project's description
└── requirements.txt        # Python dependencies (Pandas)
```

---

## Usage

Run the full pipeline:
```bash
python main.py
```

With custom files:
```bash
python main.py --input my_data.csv --output my_data_clean.csv
```

Run individual stages:
```bash
python profile.py
python validate.py
python transform.py
```
---

## License
Distributed under the MIT License. See `LICENSE` for details.