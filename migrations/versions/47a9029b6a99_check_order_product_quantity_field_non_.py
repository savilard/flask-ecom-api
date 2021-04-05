"""check order product quantity field non negative

Revision ID: 47a9029b6a99
Revises: 62371d762299
Create Date: 2021-04-05 08:43:45.226758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47a9029b6a99'
down_revision = '62371d762299'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        'check_order_product_quantity_non_negative',
        table_name='order_product',
        condition='quantity >= 0',
    )


def downgrade():
    op.drop_constraint('check_order_product_quantity_non_negative')
