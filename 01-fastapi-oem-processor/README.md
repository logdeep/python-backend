# FastAPI OEM Product Processor

A hands-on FastAPI project for validating and processing OEM product records.

## Features
- FastAPI endpoints and Pydantic validation
- Business logic separated from HTTP handlers
- Automated tests with pytest
- Interactive API docs

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs.

## Test
```bash
pytest -q
```

Next steps: CSV batch import, PostgreSQL persistence, idempotency, retries, structured logging, and CI.