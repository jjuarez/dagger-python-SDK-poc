# Dagger python SDK (PoC)

The idea behind this project is to give a try to [this](https://docs.dagger.io/sdk/python) amazing SDK with a more or less real python project that uses:
  * Using [Poetry](https://python-poetry.org) as the build and package tool
  * Using [pytest](https://pytest.org) as a Test Framework
  * Using [ruff](https://github.com/charliermarsh/ruff) as the linter tool
  * ...and using the `src` pattern, which is not used by default in poetry projects

## 🛠️ Getting Started
For now, the pipeline only implements the following commands:
  * lint
  * test

The way to use this target is as follows:
```bash
python pipeline.py (test|lint)
```

## 💡Next steps & Ideas
* Wrap all the commands of the pipeline with some python CLI framework, like [Typer,](https://typer.tiangolo.com) or [click](https://click.palletsprojects.com)

* Adding more pipeline commands, for example, build, release, etc.

