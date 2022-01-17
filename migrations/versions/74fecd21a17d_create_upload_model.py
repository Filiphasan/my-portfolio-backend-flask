"""Create upload model

Revision ID: 74fecd21a17d
Revises: 189c0962909b
Create Date: 2022-01-14 19:53:12.689858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74fecd21a17d'
down_revision = '189c0962909b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploads',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=128), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=128), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('upload_for', sa.String(length=30), nullable=True),
    sa.Column('upload_for_id', sa.String(length=128), nullable=True),
    sa.Column('filename', sa.String(length=60), nullable=False),
    sa.Column('file_path', sa.String(length=240), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uploads')
    # ### end Alembic commands ###