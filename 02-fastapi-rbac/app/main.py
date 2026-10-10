from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from app.security import USERS, current_user, issue_token, require_permission

app = FastAPI(title="RBAC API", version="1.0.0")


class TokenRequest(BaseModel):
    username: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/token")
def create_token(request: TokenRequest):
    if request.username not in USERS:
        raise HTTPException(status_code=401, detail="Unknown demo user")
    return {"access_token": issue_token(request.username), "token_type": "bearer", "role": USERS[request.username]["role"]}


@app.get("/me")
def me(user: dict = Depends(current_user)):
    return user


@app.get("/reports")
def list_reports(user: dict = Depends(require_permission("reports:read"))):
    return {"items": [{"id": 1, "title": "Quarterly summary"}], "requested_by": user["username"]}


@app.post("/reports", status_code=201)
def create_report(user: dict = Depends(require_permission("reports:write"))):
    return {"id": 2, "title": "New report", "created_by": user["username"]}


@app.delete("/reports/{report_id}")
def delete_report(report_id: int, user: dict = Depends(require_permission("reports:delete"))):
    return {"deleted_id": report_id, "deleted_by": user["username"]}
