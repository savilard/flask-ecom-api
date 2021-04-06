"""merge heads migrates

Revision ID: c050aa3236c5
Revises: a31c67668e0d, 82cd98a31152
Create Date: 2021-04-06 10:36:51.159392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c050aa3236c5'
down_revision = ('a31c67668e0d', '82cd98a31152')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
