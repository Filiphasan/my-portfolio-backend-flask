"""Create About Me Table

Revision ID: b3c8b8285d2c
Revises: 423e8f3d0b16
Create Date: 2022-01-01 20:25:22.973815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3c8b8285d2c'
down_revision = '423e8f3d0b16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_me',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=128), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=128), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('full_name', sa.String(length=70), nullable=False),
    sa.Column('job_title', sa.String(length=120), nullable=False),
    sa.Column('short_desc', sa.String(length=340), nullable=False),
    sa.Column('profile_photo', sa.String(length=250), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('short_adress', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('about_me')
    # ### end Alembic commands ###
