# CSV Data Pipeline

A lightweight ETL pipeline demonstrating data profiling, validation, and transformation using Python and pandas.

This project highlights my learning roadmap to engineer a data workflow from as basic as the foundation level.

---

## Pipeline Stages
- `profile.py`   — explores and summarises the dataset
- `validate.py`  — identifies data quality issues
- `transform.py` — cleans and normalises the data
- `main.py` — orchestrates the full pipeline end to end

---

## Tech Stack
- Python 3.10+
- pandas
- pathlib, argparse, re

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
python validator.py
python main.py
```
---

## License
Distributed under the MIT License. See `LICENSE` for details.