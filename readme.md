## Folder Structure
<pre><code>ml_project/ │ ├── data/ # Raw and processed datasets │ ├── raw/ # Untouched, original data files │ └── processed/ # Cleaned and transformed data │ ├── notebooks/ # Exploratory notebooks (EDA, prototyping) │ ├── src/ # Main source code │ ├── __init__.py │ ├── config/ # Config files and environment variables │ │ ├── paths.py │ │ └── model_config.py │ │ │ ├── data/ # Data loading and preprocessing │ │ ├── load_data.py │ │ └── preprocess.py │ │ │ ├── features/ # Feature engineering │ │ ├── build_features.py │ │ └── fourier_features.py │ │ │ ├── models/ # Model training, evaluation, prediction │ │ ├── train_model.py │ │ ├── evaluate.py │ │ └── predict.py │ │ │ ├── utils/ # Helper functions (logging, metrics, plots) │ │ ├── logger.py │ │ └── visualization.py │ │ │ └── main.py # Entry point of the ML pipeline │ ├── tests/ # Unit tests for each module │ ├── test_data.py │ └── test_models.py │ ├── outputs/ # Generated files │ ├── models/ # Trained model files │ ├── reports/ # Evaluation reports or figures │ └── logs/ # Logs from training, errors, etc. │ ├── requirements.txt # Python dependencies ├── pyproject.toml # Modern project metadata and config ├── .env # Environment-specific variables └── README.md # Project overview and instructions </code></pre>

## Way of working with uv
1. Create a new project directory and enter it.
2. Run `uv venv` to create a virtual environment.
3. Activate the environment with `source .venv/bin/activate`
4. Run `uv init` to set project metadata if you want.
5. Install packages as needed with `uv add ...`. Alternatively use `uv pip install ...`
6. Commit `pyproject.toml` and `uv.lock` to git.
7. Others can clone the repo, run `uv venv`, activate the environment and `uv sync` to get the same environment.

