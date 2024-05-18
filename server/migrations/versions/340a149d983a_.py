"""empty message

Revision ID: 340a149d983a
Revises: 
Create Date: 2024-05-16 21:36:27.337006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '340a149d983a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('loom_embed_url', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('github_link', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_project_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_portfolio',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], name=op.f('fk_user_portfolio_portfolio_id_portfolio')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_portfolio_user_id_user')),
    sa.PrimaryKeyConstraint('user_id', 'portfolio_id')
    )
    op.create_table('project_portfolio',
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], name=op.f('fk_project_portfolio_portfolio_id_portfolio')),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], name=op.f('fk_project_portfolio_project_id_project')),
    sa.PrimaryKeyConstraint('project_id', 'portfolio_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_portfolio')
    op.drop_table('user_portfolio')
    op.drop_table('project')
    op.drop_table('user')
    op.drop_table('portfolio')
    # ### end Alembic commands ###
