## Way of working with uv
1. Create a new project directory and enter it.
2. Run `uv venv` to create a virtual environment.
3. Activate the environment with `source .venv/bin/activate`
4. (Optional) Run `uv init` to set project metadata if you want.
5. Install packages as needed with `uv add ...`.
6. Commit `pyproject.toml` and `uv.lock` to git.
7. Others can clone the repo, run `uv venv`, activate the environment and `uv sync` to get the same environment.