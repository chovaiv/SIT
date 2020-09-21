"""empty message

Revision ID: 3a96a729a609
Revises: a8299cf600
Create Date: 2016-10-12 13:44:39.552653

"""

# revision identifiers, used by Alembic.
revision = '3a96a729a609'
down_revision = 'a8299cf600'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    ### end Alembic commands ###