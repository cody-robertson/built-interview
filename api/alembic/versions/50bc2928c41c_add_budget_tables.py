"""Add Budget tables

Revision ID: 50bc2928c41c
Revises: 
Create Date: 2022-07-15 02:33:54.192335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50bc2928c41c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('budget_amount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=15, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('budget_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('budget_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Numeric(precision=15, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('budget_item')
    op.drop_table('budget_category')
    op.drop_table('budget_amount')
    # ### end Alembic commands ###