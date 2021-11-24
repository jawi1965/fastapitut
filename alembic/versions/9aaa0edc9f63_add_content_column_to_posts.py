"""add content column to posts

Revision ID: 9aaa0edc9f63
Revises: 9a1f97d95db3
Create Date: 2021-11-23 13:59:59.696702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aaa0edc9f63'
down_revision = '9a1f97d95db3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
