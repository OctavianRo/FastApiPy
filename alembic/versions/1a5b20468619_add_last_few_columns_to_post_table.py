"""add last few columns to post table

Revision ID: 1a5b20468619
Revises: 9dd0e231833b
Create Date: 2023-01-07 18:14:18.791884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a5b20468619'
down_revision = '9dd0e231833b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

