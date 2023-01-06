"""Add user table

Revision ID: 571b9ce02e35
Revises: e81ef8975ab5
Create Date: 2023-01-06 22:02:53.320909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '571b9ce02e35'
down_revision = 'e81ef8975ab5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table("users")
    pass
