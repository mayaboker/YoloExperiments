# YoloExperiments

A Hydra-based foundation for reproducible data science experiments.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## Run

```bash
python3 main.py
```

Place the default CSV dataset at `data/raw/dataset.csv`, with a column named
`target`. Override configuration from the command line when needed:

```bash
python3 main.py data.file_name=my_data.csv data.target_column=label
```

Hydra stores run metadata under `outputs/`. Add configuration variants under
`configs/data/` and `configs/model/` without changing application code.
