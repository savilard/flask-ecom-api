"""check order product cost field non negative

Revision ID: 82cd98a31152
Revises: 47a9029b6a99
Create Date: 2021-04-05 08:48:48.386153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82cd98a31152'
down_revision = '47a9029b6a99'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        'check_order_product_cost_non_negative',
        table_name='order_product',
        condition='cost >= 0',
    )


def downgrade():
    op.drop_constraint('check_order_product_cost_non_negative')
