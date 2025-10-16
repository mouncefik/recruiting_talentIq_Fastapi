TalentIQ Project recuirting system!

# Install pre-commit (if not already installed)
pip install pre-commit

# Install the git hooks
pre-commit install

# Run on all files to fix any existing issues
pre-commit run --all-files


### For main dependencies:

```bash
poetry add fastapi uvicorn sqlalchemy pydantic python-multipart openai python-dotenv alembic
```
### For development dependencies:

```bash
poetry add --group dev black isort flake8 mypy pre-commit
🎯 Alternative: One Complete Command
If you want to do it all at once:
```

```bash
poetry add fastapi uvicorn sqlalchemy pydantic python-multipart openai python-dotenv alembic && poetry add --group dev black isort flake8 mypy pre-commit
```

