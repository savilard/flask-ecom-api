"""check product ingredient fields non negative

Revision ID: 5e2c167c376a
Revises: ecfd415486fa
Create Date: 2021-04-05 07:39:27.947388

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '5e2c167c376a'
down_revision = 'ecfd415486fa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        'check_ingredient_price_non_negative',
        table_name='ingredient',
        condition='price >= 0',
    )
    op.create_check_constraint(
        'check_ingredient_weight_non_negative',
        table_name='ingredient',
        condition='weight >= 0',
    )


def downgrade():
    op.drop_constraint('check_ingredient_price_non_negative')
    op.drop_constraint('check_ingredient_weight_non_negative')
