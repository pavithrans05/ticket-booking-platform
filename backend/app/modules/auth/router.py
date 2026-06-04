from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.modules.auth.dependencies import (
    get_current_user,
)

from app.modules.auth.schemas import (
    LoginRequest,
    RegisterRequest,
    RegisterResponse,
    TokenResponse,
    CurrentUserResponse,
)

from app.modules.auth.service import AuthService

from app.modules.users.models import User

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
)
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db),
):

    try:

        user = (
            AuthService(db)
            .register(
                payload.email,
                payload.full_name,
                payload.password,
            )
        )

        return RegisterResponse(
            id=user.id,
            email=user.email,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
):

    try:

        token = (
            AuthService(db)
            .login(
                payload.email,
                payload.password,
            )
        )

        return TokenResponse(
            access_token=token,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.post(
    "/token",
    response_model=TokenResponse,
)
def token_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    try:

        token = (
            AuthService(db)
            .login(
                form_data.username,
                form_data.password,
            )
        )

        return TokenResponse(
            access_token=token,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=CurrentUserResponse,
)
def me(
    current_user: User = Depends(
        get_current_user
    ),
):

    return CurrentUserResponse(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
    )