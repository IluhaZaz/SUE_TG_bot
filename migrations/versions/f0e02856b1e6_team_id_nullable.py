"""team_id nullable

Revision ID: f0e02856b1e6
Revises: 903ca176ecd2
Create Date: 2025-04-13 20:45:08.291526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0e02856b1e6'
down_revision: Union[str, None] = '903ca176ecd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'team_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'team_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
