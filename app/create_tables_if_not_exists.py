from app import db_conn
from sqlalchemy import inspect


def create_table_if_not_exists(class_name, table_name):
    if inspect(db_conn.engine).has_table(table_name, schema="torqata_data_ip"):
        print('Table %s exists' % table_name)
    else:
        class_name.__table__.create(db_conn.engine)
