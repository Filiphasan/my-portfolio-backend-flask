"""Create interest table

Revision ID: c8e3c1ccaca6
Revises: 3b1e48405fac
Create Date: 2022-01-03 21:15:24.949844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e3c1ccaca6'
down_revision = '3b1e48405fac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interests',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=128), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=128), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=240), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interests')
    # ### end Alembic commands ###