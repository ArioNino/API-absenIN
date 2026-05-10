"""users columns not null

Revision ID: a1b2c3d4e5f6
Revises: f90154a33b37
Create Date: 2026-05-10 21:35:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = 'f90154a33b37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema.

    Sync the `users` table with the ORM: make email/password/name NOT NULL.
    Any pre-existing NULL values are backfilled with empty strings before
    applying the constraint so the ALTER does not fail on dirty rows. Rows
    with blank credentials will fail to authenticate, which is the desired
    outcome for such data.
    """
    op.execute("UPDATE users SET email = '' WHERE email IS NULL")
    op.execute("UPDATE users SET password = '' WHERE password IS NULL")
    op.execute("UPDATE users SET name = '' WHERE name IS NULL")

    op.alter_column(
        'users', 'email',
        existing_type=sa.String(length=100),
        nullable=False,
    )
    op.alter_column(
        'users', 'password',
        existing_type=sa.String(length=255),
        nullable=False,
    )
    op.alter_column(
        'users', 'name',
        existing_type=sa.String(length=100),
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'users', 'name',
        existing_type=sa.String(length=100),
        nullable=True,
    )
    op.alter_column(
        'users', 'password',
        existing_type=sa.String(length=255),
        nullable=True,
    )
    op.alter_column(
        'users', 'email',
        existing_type=sa.String(length=100),
        nullable=True,
    )
