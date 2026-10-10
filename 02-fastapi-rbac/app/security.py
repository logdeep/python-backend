import os
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

JWT_SECRET = os.getenv("JWT_SECRET", "local-development-only-change-me")
JWT_ALGORITHM = "HS256"
BEARER = HTTPBearer(auto_error=False)

USERS = {
    "alice": {"role": "admin"},
    "ben": {"role": "editor"},
    "cara": {"role": "viewer"},
}
ROLE_PERMISSIONS = {
    "admin": {"reports:read", "reports:write", "reports:delete"},
    "editor": {"reports:read", "reports:write"},
    "viewer": {"reports:read"},
}


def issue_token(username: str) -> str:
    user = USERS.get(username)
    if user is None:
        raise ValueError("Unknown demo user")
    now = datetime.now(timezone.utc)
    payload = {"sub": username, "role": user["role"], "iat": now, "exp": now + timedelta(minutes=30)}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def current_user(credentials: HTTPAuthorizationCredentials | None = Depends(BEARER)) -> dict:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Bearer token required", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username, role = payload.get("sub"), payload.get("role")
        if username not in USERS or USERS[username]["role"] != role:
            raise jwt.InvalidTokenError("Unknown user or role mismatch")
        return {"username": username, "role": role}
    except jwt.InvalidTokenError as exc:
        raise HTTPException(status_code=401, detail="Invalid or expired token", headers={"WWW-Authenticate": "Bearer"}) from exc


def require_permission(permission: str):
    def dependency(user: dict = Depends(current_user)) -> dict:
        if permission not in ROLE_PERMISSIONS.get(user["role"], set()):
            raise HTTPException(status_code=403, detail="Insufficient permission")
        return user
    return dependency
