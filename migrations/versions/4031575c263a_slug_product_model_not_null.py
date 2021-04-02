"""slug product model not null

Revision ID: 4031575c263a
Revises: 8cb7b2ba1d54
Create Date: 2021-04-02 15:38:05.905981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4031575c263a'
down_revision = '8cb7b2ba1d54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category', 'slug',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    op.drop_constraint('category_slug_key', 'category', type_='unique')
    op.alter_column('product', 'slug',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'slug',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.create_unique_constraint('category_slug_key', 'category', ['slug'])
    op.alter_column('category', 'slug',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    # ### end Alembic commands ###