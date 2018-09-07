"""added a column that stores author,pitch and password

Revision ID: 2340d9229651
Revises: bb70d539a3aa
Create Date: 2018-09-07 12:21:48.406584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2340d9229651'
down_revision = 'bb70d539a3aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('author', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitchs', 'users', ['author'], ['id'])
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    op.drop_constraint(None, 'pitchs', type_='foreignkey')
    op.drop_column('pitchs', 'author')
    # ### end Alembic commands ###