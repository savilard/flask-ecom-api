"""add last migrate

Revision ID: 8cb7b2ba1d54
Revises: 6d99551dc1cd
Create Date: 2021-03-29 14:52:04.245794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cb7b2ba1d54'
down_revision = '6d99551dc1cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_order_customer_id'), 'order', ['customer_id'], unique=False)
    op.create_foreign_key(None, 'order', 'customer', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_index(op.f('ix_order_customer_id'), table_name='order')
    op.drop_column('order', 'customer_id')
    # ### end Alembic commands ###
