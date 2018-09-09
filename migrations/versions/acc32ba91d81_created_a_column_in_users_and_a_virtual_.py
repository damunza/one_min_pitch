"""created a column in users and a virtual column in pitchs

Revision ID: acc32ba91d81
Revises: ee526d8e7b07
Create Date: 2018-09-09 08:39:34.719563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acc32ba91d81'
down_revision = 'ee526d8e7b07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pitchs_author_fkey', 'pitchs', type_='foreignkey')
    op.drop_column('pitchs', 'author')
    op.add_column('users', sa.Column('pitch', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'pitchs', ['pitch'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'pitch')
    op.add_column('pitchs', sa.Column('author', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitchs_author_fkey', 'pitchs', 'users', ['author'], ['id'])
    # ### end Alembic commands ###
