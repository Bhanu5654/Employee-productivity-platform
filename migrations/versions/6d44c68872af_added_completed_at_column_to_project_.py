"""Added completed_at column to Project table

Revision ID: 6d44c68872af
Revises: 
Create Date: 2025-02-16 11:18:12.801307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d44c68872af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('file_path',
               existing_type=sa.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('assigned_by',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('approved')
        batch_op.drop_column('submission_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('submission_file', sa.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('approved', sa.BOOLEAN(), nullable=True))
        batch_op.alter_column('assigned_by',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('file_path',
               existing_type=sa.String(length=255),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.drop_column('completed_at')

    # ### end Alembic commands ###
