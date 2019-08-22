"""create todos table

Revision ID: f2bdd35622cd
Revises: 
Create Date: 2018-10-22 14:02:12.538877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2bdd35622cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'todos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('todo', sa.String(100), nullable=False),
        sa.Column('note', sa.Unicode(250)),
        sa.Column('status', sa.Integer),
    )


def downgrade():
    op.drop_table('todos')
