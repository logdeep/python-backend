# Django Inventory API

A Django REST Framework API for a small inventory workflow. It demonstrates relational models, serializers, querysets, validation, and API tests.

## Features
- Product records with SKU, price, and stock count
- Order creation that validates stock and decreases inventory atomically
- Read endpoints for products and orders
- Django ORM and SQLite for a zero-setup local database

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Browse http://127.0.0.1:8000/api/products/.

## Test
Run `pytest -q`.

## Notes
This is a learning example. For production, add authentication, pagination, database-backed migrations review, currency-safe decimal handling, and a proper order lifecycle.
