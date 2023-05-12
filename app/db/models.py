from enum import Enum, unique

from sqlalchemy import (
    Column, Date, Enum as SaEnum, Integer,
    MetaData, String, Table,
)

from app.config import DATABASE_VARIANT


# https://docs.sqlalchemy.org/en/13/core/constraints.html#configuring-constraint-naming-conventions
convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)


@unique
class Gender(Enum):
    female = 'female'
    male = 'male'


if not DATABASE_VARIANT:
    user_table = Table(
        'users',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('birth_date', Date, nullable=False),
        Column('gender', SaEnum(Gender, name='gender'), nullable=False),
        # Column('exampl_1', String),
        # Column('exampl_2', Integer),
    )
elif DATABASE_VARIANT == 1:
    user_table = Table(
        'users',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('birth_date', Date, nullable=False),
        Column('gender', SaEnum(Gender, name='gender'), nullable=False),
        Column('exampl_1', String),
        # Column('exampl_2', Integer),
    )
elif DATABASE_VARIANT == 2:
    user_table = Table(
        'users',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('birth_date', Date, nullable=False),
        Column('gender', SaEnum(Gender, name='gender'), nullable=False),
        Column('exampl_1', String),
        Column('exampl_2', Integer),
    )
