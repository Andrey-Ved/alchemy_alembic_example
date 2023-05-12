from sqlalchemy.sql import text
from sqlalchemy import MetaData, create_engine, select, insert

import os

from app.config import DATABASE_NAME
from app.db.models import metadata, user_table, Gender


class DataBase:
    def __init__(self):
        self.alembic_migrations()

        self.engine = create_engine(
            f'sqlite:///{DATABASE_NAME}',
            echo=False
        )

        self.engine.connect()
        self.metadata = metadata

        self.users = user_table

    @staticmethod
    def alembic_migrations():
        os.system('alembic revision --autogenerate -m "auto"')
        os.system("alembic upgrade heads")

    def clear_db(self):
        meta = MetaData()
        meta.reflect(bind=self.engine)

        with self.engine.connect() as conn:
            trans = conn.begin()

            for table in meta.sorted_tables:
                if str(table) != 'alembic_version':
                    conn.execute(table.delete())

            trans.commit()

    def _id_search_with_insert(self, table, row, row_at_creating=None):
        table_name = str(table.name)
        where = "AND ".join(
            f'{table_name}.{k} = "{row[k]}" '
            for k in row
        )

        s = text(f'SELECT {table_name}.id FROM {table_name} WHERE {where} ')

        with self.engine.connect() as conn:
            rs = conn.execute(s)

        row_id = rs.first()

        if not row_id:

            if row_at_creating:
                row.update(row_at_creating)

            s = insert(table).values(row)

            with self.engine.connect() as conn:
                rs = conn.execute(s)
                conn.commit()

            row_id = rs.inserted_primary_key

        return row_id[0]

    def create(self, user):
        return self._id_search_with_insert(self.users, user)

    def read(self, user_id):
        s = select(self.users)\
            .where(self.users.c.id == int(user_id))

        rows = []
        with self.engine.connect() as conn:
            for row in conn.execute(s):
                rows.append(
                    dict(row._mapping)
                )
                rows[-1]['gender'] = Gender(rows[-1]['gender']).name

        return rows
