"""Create table Product

Revision ID: 6b107302943f
Revises: 2c9e53128176
Create Date: 2024-12-07 19:45:38.775315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b107302943f'
down_revision = '2c9e53128176'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nama', sa.String(length=230), nullable=False),
    sa.Column('harga', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('kategori_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['kategori_id'], ['category_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_product_updated_at'), ['updated_at'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_updated_at'))
        batch_op.drop_index(batch_op.f('ix_product_created_at'))

    op.drop_table('product')
    # ### end Alembic commands ###
