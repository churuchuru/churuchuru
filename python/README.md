# Python Training

This project uses `uv` for environment management.

## Setup

1. **Install uv**:

   If you don't have `uv` installed, you can install it either with `pip` or `brew`:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   ```bash
   brew install uv
   ```

2. **Install dependencies**:

   The dependencies are listed in `pyproject.toml`. To install them, run:

   ```bash
   uv sync
   ```

3. **Activate the virtual environment**:

   ```bash
   source .venv/bin/activate
   ```

## Managing Dependencies

To add more packages, add them to the `dependencies` list in `pyproject.toml`. Then, re-run the sync command to update your environment:

```bash
uv sync
```

## Format, Linting, and Type Check

For format

```bash
ruff format
```

For linting

```bash
ruff check
```

For type checking

```bash
ty check
```

## Unit Testing

```bash
pytest
```

## Launch Marimo

```bash
marimo edit
```
