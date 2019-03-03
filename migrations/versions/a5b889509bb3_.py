"""empty message

Revision ID: a5b889509bb3
Revises: 
Create Date: 2019-03-03 02:09:42.315381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5b889509bb3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.DateTime(), onupdate=sa.ColumnDefault(sa.sql.functions.now()), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'username'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donation')
    op.drop_table('user')
    op.drop_table('organization')
    # ### end Alembic commands ###
