# Python Backend Interview Projects

Hands-on backend projects built with Python, FastAPI, and Django to demonstrate API design, validation, authentication, authorization, data processing, persistence, and testing.

## Projects

### 1. FastAPI OEM Product Processor
`01-fastapi-oem-processor/`

A REST API that validates OEM product records and calculates total product value. Includes Pydantic schemas, a separate service layer, health endpoint, and pytest API tests.

- [Project README](01-fastapi-oem-processor/README.md)
- Stack: Python, FastAPI, Pydantic, pytest
- Planned extensions: CSV batch ingestion, PostgreSQL, idempotency, retries, structured logging, CI

### Planned

- **FastAPI RBAC API** — JWT authentication, role/permission mapping, and authorization tests.
- **Django Inventory API** — Django REST Framework, relational models, products, orders, and ORM queries.

## General goals
Each project will include setup instructions, sample requests, automated tests, and notes on design decisions. Projects are intended as practical interview-preparation exercises.
