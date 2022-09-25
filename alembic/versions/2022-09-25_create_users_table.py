"""create users table

Revision ID: 2da981e96f12
Revises: 
Create Date: 2022-09-25 12:43:03.514935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2da981e96f12"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String(255), nullable=False, unique=True, index=True),
        sa.Column("email", sa.String(255), nullable=False, unique=True, index=True),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("avatar", sa.String(255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("users")
