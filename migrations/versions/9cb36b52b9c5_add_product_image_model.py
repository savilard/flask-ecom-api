"""add product_image model

Revision ID: 9cb36b52b9c5
Revises: 52c5cd419332
Create Date: 2021-03-23 16:05:40.731083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb36b52b9c5'
down_revision = '52c5cd419332'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src', sa.String(length=140), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_image_product_id'), 'product_image', ['product_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_image_product_id'), table_name='product_image')
    op.drop_table('product_image')
    # ### end Alembic commands ###