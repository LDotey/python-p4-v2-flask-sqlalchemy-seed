"""Initial migration

Revision ID: 336fce6d24c4
Revises: 
Create Date: 2024-11-08 14:02:25.648184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336fce6d24c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
