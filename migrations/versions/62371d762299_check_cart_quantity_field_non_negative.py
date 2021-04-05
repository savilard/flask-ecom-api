"""check cart quantity field non negative

Revision ID: 62371d762299
Revises: 5e2c167c376a
Create Date: 2021-04-05 07:51:54.085829

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '62371d762299'
down_revision = '5e2c167c376a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        'check_cart_product_quantity_non_negative',
        table_name='cart_product',
        condition='quantity >= 0',
    )


def downgrade():
    op.drop_constraint('check_cart_product_quantity_non_negative')
