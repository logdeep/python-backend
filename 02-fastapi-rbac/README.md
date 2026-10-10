# FastAPI RBAC API

A small role-based access control API designed to make authentication and authorization easy to reason about. It demonstrates the difference between identifying a caller and checking whether that caller can perform an action.

## Features
- Bearer-token authentication using signed JWTs
- Role-to-permission mapping centralized in one module
- Protected endpoints with clear 401 vs 403 behavior
- Tests for allowed and denied access

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Demo credentials
The demo endpoint issues short-lived tokens for the sample users `alice` (admin), `ben` (editor), and `cara` (viewer). This user store and signing key are for local learning only; do not deploy them. Configure a strong secret via `JWT_SECRET` outside development.

## Permission behavior
- `GET /reports`: any authenticated role
- `POST /reports`: admin or editor
- `DELETE /reports/{report_id}`: admin only

A missing or invalid token returns 401. A valid token without the required permission returns 403, not a redirect to a login page. This is appropriate for an API client.

## Test
Run `pytest -q`.
