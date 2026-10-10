# Python Backend Interview Projects

Hands-on portfolio projects built with Python, FastAPI, and Django. Each folder is a self-contained exercise with setup instructions and tests.

## Projects

### 1. [FastAPI OEM Product Processor](./01-fastapi-oem-processor/)
Validates OEM product payloads with Pydantic and calculates total product value in a separate service layer. Includes health endpoint and API tests.

**Stack:** FastAPI, Pydantic, pytest

### 2. [FastAPI RBAC API](./02-fastapi-rbac/)
Demonstrates JWT bearer authentication, centralized role-to-permission mapping, protected endpoints, and API-appropriate `401 Unauthorized` versus `403 Forbidden` responses.

**Stack:** FastAPI, PyJWT, pytest

Demo identities are provided for local learning only. The default signing secret is not production-safe; set `JWT_SECRET` before using outside local development.

### 3. [Django Inventory API](./03-django-inventory-api/)
Provides product and order endpoints with Django ORM models, serializers, stock validation, and transactional order creation.

**Stack:** Django, Django REST Framework, SQLite, pytest-django

## How to use this repository

1. Choose a project folder.
2. Follow that folder's README to create a virtual environment and install dependencies.
3. Run its tests with `pytest -q`.
4. Start the API and explore endpoints through the docs or the included endpoint instructions.

Each project uses synthetic example data. These are interview-practice examples, not production-ready systems. Useful next steps include CI, environment-based configuration, authentication for the inventory API, PostgreSQL, migrations, and deployment.
