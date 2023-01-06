"""add content columns to posts table

Revision ID: e81ef8975ab5
Revises: b4dd31e0e038
Create Date: 2023-01-06 21:58:01.719068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e81ef8975ab5'
down_revision = 'b4dd31e0e038'
branch_labels = None
depends_on = None


def upgrade():
    # add in the logic to add a new column 
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
