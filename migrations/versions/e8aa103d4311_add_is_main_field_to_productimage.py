"""add is_main field to ProductImage

Revision ID: e8aa103d4311
Revises: 59d18ec245f4
Create Date: 2021-03-26 12:54:51.797389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8aa103d4311'
down_revision = '59d18ec245f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_image', sa.Column('is_main', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_image', 'is_main')
    # ### end Alembic commands ###
