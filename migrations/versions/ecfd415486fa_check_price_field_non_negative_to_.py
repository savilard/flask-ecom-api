"""check price field non negative to product

Revision ID: ecfd415486fa
Revises: 7a3228322f8b
Create Date: 2021-04-05 07:30:03.405246

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'ecfd415486fa'
down_revision = '7a3228322f8b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        'check_product_price_non_negative',
        table_name='product',
        condition='price >= 0',
    )


def downgrade():
    op.drop_constraint('check_product_price_non_negative')
