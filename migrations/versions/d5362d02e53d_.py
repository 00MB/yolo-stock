"""empty message

Revision ID: d5362d02e53d
Revises: 3a7bd9be691d
Create Date: 2021-03-07 03:22:29.233450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5362d02e53d'
down_revision = '3a7bd9be691d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bank_balance', sa.Float(), server_default='0', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'bank_balance')
    # ### end Alembic commands ###
