## Folder Structure
```bash
probabilistic_spread_forecasting/
├── data/                    # Raw and processed datasets
│   ├── raw/                 # Untouched, original data files
│   └── processed/           # Cleaned and transformed data
│
├── notebooks/               # Exploratory notebooks (EDA, prototyping, experimenting)
│
├── src/                     # Main source code
│   ├── __init__.py
│   ├── config/              # Config files and environment variables
│   │
│   ├── data/                # Data loading and preprocessing
│   │
│   ├── features/            # Feature engineering
│   │
│   ├── models/              # Model training, evaluation, prediction
│   │
│   ├── utils/               # Helper functions (logging, metrics, plots)
│   │
│   └── main.py              # Entry point of the ML pipeline
│
├── tests/                   # Unit tests for each module
│
├── outputs/                 # Generated files
│   ├── models/              # Trained model files
│   ├── reports/             # Evaluation reports or figures
│   └── logs/                # Logs from training, errors, etc.
│
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Modern project metadata and config
├── .env                     # Environment-specific variables
└── README.md                # Project overview and instructions
```


## Way of working with uv
1. Create a new project directory and enter it.
2. Run `uv venv` to create a virtual environment.
3. Activate the environment with `source .venv/bin/activate`
4. Run `uv init` to set project metadata if you want.
5. Install packages as needed with `uv add ...`. Alternatively use `uv pip install ...`
6. Commit `pyproject.toml` and `uv.lock` to git.
7. Others can clone the repo, run `uv venv`, activate the environment and `uv sync` to get the same environment.

## Resources used
1. Benchmark different FE techniques: https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py


