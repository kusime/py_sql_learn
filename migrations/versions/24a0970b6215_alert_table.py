"""alert table

Revision ID: 24a0970b6215
Revises: 790b229897e2
Create Date: 2024-06-04 21:53:19.913277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24a0970b6215'
down_revision: Union[str, None] = '790b229897e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('csv_import_test', sa.Column('data2', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('csv_import_test', 'data2')
    # ### end Alembic commands ###
