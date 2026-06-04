from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.jwt import decode_token

from app.modules.users.models import User

from app.modules.roles.repository import (
    RoleRepository,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):

    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user_id = payload.get("sub")

    user = (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user


def require_admin(
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db),
):

    roles = (
        RoleRepository(db)
        .get_user_roles(
            current_user.id
        )
    )

    role_names = [
        role.name
        for role in roles
    ]

    if "ADMIN" not in role_names:
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    return current_user