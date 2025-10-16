# TalentIQ - Recruiting System

A modern recruiting platform built with FastAPI, SQLAlchemy, and PostgreSQL. This application provides a RESTful API for managing recruitment processes with features including job postings, candidate tracking, and interview scheduling.

## Tech Stack

- **Backend**: FastAPI (Python web framework)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Migration**: Alembic for database schema management
- **Package Management**: Poetry for dependency management
- **Code Quality**: Pre-commit hooks with Black, isort, flake8, and mypy

## Quick Start

1. **Install dependencies**: `poetry install`
2. **Set up database**: Update `.env` with your PostgreSQL credentials
3. **Run migrations**: `poetry run alembic upgrade head`
4. **Start server**: `poetry run uvicorn app.main:app --reload`

The API will be available at `http://localhost:8000` with automatic API documentation at `/docs`.
