"""edit phone column

Revision ID: 189c0962909b
Revises: d19816f1fa00
Create Date: 2022-01-14 19:31:53.551472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '189c0962909b'
down_revision = 'd19816f1fa00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('about_me', 'phone_number',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=25),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('about_me', 'phone_number',
               existing_type=sa.String(length=25),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)
    # ### end Alembic commands ###
