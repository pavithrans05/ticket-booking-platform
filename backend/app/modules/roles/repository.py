from sqlalchemy.orm import Session

from app.modules.roles.models import Role
from app.modules.roles.user_role_model import UserRole


class RoleRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_by_name(
        self,
        name: str,
    ):
        return (
            self.db.query(Role)
            .filter(Role.name == name)
            .first()
        )

    def assign_role(
        self,
        user_id: int,
        role_id: int,
    ):
        user_role = UserRole(
            user_id=user_id,
            role_id=role_id,
        )

        self.db.add(user_role)
        self.db.commit()

        return user_role

    def get_user_roles(
        self,
        user_id: int,
    ):
        return (
            self.db.query(Role)
            .join(
                UserRole,
                Role.id == UserRole.role_id,
            )
            .filter(
                UserRole.user_id == user_id
            )
            .all()
        )