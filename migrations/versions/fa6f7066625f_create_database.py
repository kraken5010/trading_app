"""Create database

Revision ID: fa6f7066625f
Revises: 
Create Date: 2023-03-10 21:48:37.023085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa6f7066625f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
