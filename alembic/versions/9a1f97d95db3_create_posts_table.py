"""create  posts table

Revision ID: 9a1f97d95db3
Revises: 
Create Date: 2021-11-23 12:48:29.792412

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '9a1f97d95db3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                             sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
