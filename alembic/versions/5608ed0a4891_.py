"""

Revision ID: 5608ed0a4891
Revises: 
Create Date: 2025-01-10 00:10:37.500042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5608ed0a4891'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gov_welfare',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('user_type', sa.Text(), nullable=True),
    sa.Column('service_name', sa.Text(), nullable=True),
    sa.Column('service_summary', sa.Text(), nullable=True),
    sa.Column('service_category', sa.Text(), nullable=True),
    sa.Column('service_conditions', sa.Text(), nullable=True),
    sa.Column('offc_name', sa.Text(), nullable=True),
    sa.Column('dept_name', sa.Text(), nullable=True),
    sa.Column('dept_type', sa.Text(), nullable=True),
    sa.Column('dept_code', sa.Text(), nullable=True),
    sa.Column('apply_period', sa.Text(), nullable=True),
    sa.Column('apply_method', sa.Text(), nullable=True),
    sa.Column('apply_url', sa.Text(), nullable=True),
    sa.Column('document', sa.Text(), nullable=True),
    sa.Column('receiving_agency', sa.Text(), nullable=True),
    sa.Column('contact', sa.Text(), nullable=True),
    sa.Column('support_details', sa.Text(), nullable=True),
    sa.Column('support_targets', sa.Text(), nullable=True),
    sa.Column('support_type', sa.Text(), nullable=True),
    sa.Column('detail_url', sa.Text(), nullable=True),
    sa.Column('law', sa.Text(), nullable=True),
    sa.Column('JA0110', sa.Integer(), nullable=True, comment='Start Age'),
    sa.Column('JA0111', sa.Integer(), nullable=True, comment='End Age'),
    sa.Column('JA0101', sa.Boolean(), nullable=True, comment='Is for Male'),
    sa.Column('JA0102', sa.Boolean(), nullable=True, comment='Is for Female'),
    sa.Column('JA0201', sa.Boolean(), nullable=True, comment='Income is lte 50%'),
    sa.Column('JA0202', sa.Boolean(), nullable=True, comment='Income is gte 51% and lte 75%'),
    sa.Column('JA0203', sa.Boolean(), nullable=True, comment='Income is gte 76% and lte 100%'),
    sa.Column('JA0204', sa.Boolean(), nullable=True, comment='Income is gte 101% and lte 200%'),
    sa.Column('JA0205', sa.Boolean(), nullable=True, comment='Income is gte 201%'),
    sa.Column('JA0301', sa.Boolean(), nullable=True, comment='Prospective parents / Infertility'),
    sa.Column('JA0302', sa.Boolean(), nullable=True, comment='Pregnant women'),
    sa.Column('JA0303', sa.Boolean(), nullable=True, comment='Childbirth / Adoption'),
    sa.Column('JA0313', sa.Boolean(), nullable=True, comment='Farmers'),
    sa.Column('JA0314', sa.Boolean(), nullable=True, comment='Fishermen'),
    sa.Column('JA0315', sa.Boolean(), nullable=True, comment='Livestock farmers'),
    sa.Column('JA0316', sa.Boolean(), nullable=True, comment='Forestry workers'),
    sa.Column('JA0317', sa.Boolean(), nullable=True, comment='Elementary school students'),
    sa.Column('JA0318', sa.Boolean(), nullable=True, comment='Middle school students'),
    sa.Column('JA0319', sa.Boolean(), nullable=True, comment='High school students'),
    sa.Column('JA0320', sa.Boolean(), nullable=True, comment='University students / Graduate students'),
    sa.Column('JA0322', sa.Boolean(), nullable=True, comment='Not applicable'),
    sa.Column('JA0326', sa.Boolean(), nullable=True, comment='Workers / Office employees'),
    sa.Column('JA0327', sa.Boolean(), nullable=True, comment='Job seekers / Unemployed'),
    sa.Column('JA0328', sa.Boolean(), nullable=True, comment='People with disabilities'),
    sa.Column('JA0329', sa.Boolean(), nullable=True, comment='Veterans'),
    sa.Column('JA0330', sa.Boolean(), nullable=True, comment='Patients / People with diseases'),
    sa.Column('JA0401', sa.Boolean(), nullable=True, comment='Multicultural families'),
    sa.Column('JA0402', sa.Boolean(), nullable=True, comment='North Korean defectors'),
    sa.Column('JA0403', sa.Boolean(), nullable=True, comment='Single-parent / Grandparent families'),
    sa.Column('JA0404', sa.Boolean(), nullable=True, comment='Single-person households'),
    sa.Column('JA0410', sa.Boolean(), nullable=True, comment='Not applicable'),
    sa.Column('JA0411', sa.Boolean(), nullable=True, comment='Multi Child Family'),
    sa.Column('JA0412', sa.Boolean(), nullable=True, comment='Homeless households'),
    sa.Column('JA0413', sa.Boolean(), nullable=True, comment='New residents'),
    sa.Column('JA0414', sa.Boolean(), nullable=True, comment='Extended families'),
    sa.Column('JA1101', sa.Boolean(), nullable=True, comment='Prospective entrepreneurs'),
    sa.Column('JA1102', sa.Boolean(), nullable=True, comment='Currently operating businesses'),
    sa.Column('JA1103', sa.Boolean(), nullable=True, comment='Financially struggling / Closing businesses'),
    sa.Column('JA1201', sa.Boolean(), nullable=True, comment='Food service industry'),
    sa.Column('JA1202', sa.Boolean(), nullable=True, comment='Manufacturing industry'),
    sa.Column('JA1299', sa.Boolean(), nullable=True, comment='Other industries'),
    sa.Column('JA2101', sa.Boolean(), nullable=True, comment='Small and medium enterprises (SMEs)'),
    sa.Column('JA2102', sa.Boolean(), nullable=True, comment='Social welfare facilities'),
    sa.Column('JA2103', sa.Boolean(), nullable=True, comment='Institutions / Organizations'),
    sa.Column('JA2201', sa.Boolean(), nullable=True, comment='Manufacturing industry'),
    sa.Column('JA2202', sa.Boolean(), nullable=True, comment='Agriculture, forestry, and fishery'),
    sa.Column('JA2203', sa.Boolean(), nullable=True, comment='Information and communication industry'),
    sa.Column('JA2299', sa.Boolean(), nullable=True, comment='Other industries'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_for_business', 'gov_welfare', ['JA1101', 'JA1102', 'JA1103', 'JA1201', 'JA1202', 'JA1299'], unique=False)
    op.create_index('ix_for_education', 'gov_welfare', ['JA0317', 'JA0318', 'JA0319', 'JA0320', 'JA0322'], unique=False)
    op.create_index('ix_for_family', 'gov_welfare', ['JA0401', 'JA0402', 'JA0403', 'JA0404', 'JA0410', 'JA0411', 'JA0412', 'JA0413', 'JA0414'], unique=False)
    op.create_index('ix_for_life', 'gov_welfare', ['JA0301', 'JA0302', 'JA0303'], unique=False)
    op.create_index('ix_for_organization', 'gov_welfare', ['JA2101', 'JA2102', 'JA2103', 'JA2201', 'JA2202', 'JA2203', 'JA2299'], unique=False)
    op.create_index('ix_for_overcome', 'gov_welfare', ['JA0201', 'JA0202', 'JA0203', 'JA0204', 'JA0205'], unique=False)
    op.create_index('ix_for_primary_industry', 'gov_welfare', ['JA0313', 'JA0314', 'JA0315', 'JA0316'], unique=False)
    op.create_index(op.f('ix_gov_welfare_JA0110'), 'gov_welfare', ['JA0110'], unique=False)
    op.create_index(op.f('ix_gov_welfare_JA0111'), 'gov_welfare', ['JA0111'], unique=False)
    op.create_index(op.f('ix_gov_welfare_dept_type'), 'gov_welfare', ['dept_type'], unique=False)
    op.create_index(op.f('ix_gov_welfare_views'), 'gov_welfare', ['views'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('resignation_reason', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('profile', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='profiles_user_id_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('overcome', sa.Integer(), nullable=True),
    sa.Column('multicultural', sa.Boolean(), nullable=False),
    sa.Column('north_korean', sa.Boolean(), nullable=False),
    sa.Column('single_parent_or_grandparent', sa.Boolean(), nullable=False),
    sa.Column('homeless', sa.Boolean(), nullable=False),
    sa.Column('new_resident', sa.Boolean(), nullable=False),
    sa.Column('multi_child_family', sa.Boolean(), nullable=False),
    sa.Column('single_family', sa.Boolean(), nullable=False),
    sa.Column('extend_family', sa.Boolean(), nullable=False),
    sa.Column('life_status', sa.Integer(), nullable=False),
    sa.Column('primary_industry_status', sa.Integer(), nullable=False),
    sa.Column('academic_status', sa.Integer(), nullable=False),
    sa.Column('working_status', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='profiles_user_id_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_data')
    op.drop_table('profile')
    op.drop_table('user')
    op.drop_index(op.f('ix_gov_welfare_views'), table_name='gov_welfare')
    op.drop_index(op.f('ix_gov_welfare_dept_type'), table_name='gov_welfare')
    op.drop_index(op.f('ix_gov_welfare_JA0111'), table_name='gov_welfare')
    op.drop_index(op.f('ix_gov_welfare_JA0110'), table_name='gov_welfare')
    op.drop_index('ix_for_primary_industry', table_name='gov_welfare')
    op.drop_index('ix_for_overcome', table_name='gov_welfare')
    op.drop_index('ix_for_organization', table_name='gov_welfare')
    op.drop_index('ix_for_life', table_name='gov_welfare')
    op.drop_index('ix_for_family', table_name='gov_welfare')
    op.drop_index('ix_for_education', table_name='gov_welfare')
    op.drop_index('ix_for_business', table_name='gov_welfare')
    op.drop_table('gov_welfare')
    # ### end Alembic commands ###