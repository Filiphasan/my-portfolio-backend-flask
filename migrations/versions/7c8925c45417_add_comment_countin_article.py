"""add comment countin article

Revision ID: 7c8925c45417
Revises: aa79ddca3b01
Create Date: 2022-01-12 12:46:36.877017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c8925c45417'
down_revision = 'aa79ddca3b01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('comment_count', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'comment_count')
    # ### end Alembic commands ###
