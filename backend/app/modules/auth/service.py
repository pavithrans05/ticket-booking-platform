from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.core.security import hash_password
from app.core.security import verify_password

from app.modules.users.models import User
from app.modules.users.repository import UserRepository

from app.modules.roles.repository import (
    RoleRepository,
)


class AuthService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = UserRepository(db)

    def register(
        self,
        email: str,
        full_name: str,
        password: str,
    ):

        existing_user = (
            self.repository.get_by_email(
                email
            )
        )

        if existing_user:
            raise ValueError(
                "Email already registered"
            )

        user = User(
            email=email,
            full_name=full_name,
            password_hash=hash_password(
                password
            ),
        )

        user = self.repository.create(
            user
        )

        role_repository = RoleRepository(
            self.repository.db
        )

        user_role = (
            role_repository.get_by_name(
                "USER"
            )
        )

        if user_role:
            role_repository.assign_role(
                user.id,
                user_role.id,
            )

        return user

    def login(
        self,
        email: str,
        password: str,
    ):

        user = (
            self.repository.get_by_email(
                email
            )
        )

        if not user:
            raise ValueError(
                "Invalid credentials"
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid credentials"
            )

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return token