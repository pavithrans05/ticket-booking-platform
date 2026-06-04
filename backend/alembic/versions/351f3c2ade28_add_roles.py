"""add_roles

Revision ID: 351f3c2ade28
Revises: 97c9593384a0
Create Date: 2026-06-03 15:33:00.455311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "351f3c2ade28"
down_revision: Union[str, None] = "97c9593384a0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "roles",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.String(length=50),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    op.create_table(
        "user_roles",
        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "role_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
        ),
        sa.PrimaryKeyConstraint(
            "user_id",
            "role_id",
        ),
    )

    role_table = sa.table(
        "roles",
        sa.column(
            "name",
            sa.String,
        ),
    )

    op.bulk_insert(
        role_table,
        [
            {"name": "ADMIN"},
            {"name": "USER"},
        ],
    )


def downgrade() -> None:

    op.drop_table("user_roles")
    op.drop_table("roles")