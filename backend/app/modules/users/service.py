from sqlalchemy.orm import Session

from app.modules.users.models import User
from app.modules.users.repository import UserRepository
from app.modules.users.schemas import UserCreate


class UserService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = UserRepository(db)

    def create_user(
        self,
        payload: UserCreate,
    ):
        user = User(
            email=payload.email,
            full_name=payload.full_name,
            password_hash=payload.password,
        )

        return self.repository.create(user)