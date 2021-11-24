"""add foreign key to post table

Revision ID: 6f953d61fac3
Revises: c28b4e98d511
Create Date: 2021-11-23 16:11:04.944894

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import ForeignKeyConstraint


# revision identifiers, used by Alembic.
revision = '6f953d61fac3'
down_revision = 'c28b4e98d511'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                    sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
                   
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
