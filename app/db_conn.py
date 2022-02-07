from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.config import load_settings

engine = create_engine(load_settings.conn_uri)
Session = sessionmaker(bind=engine)


def session_conn():
    session = Session()
    try:
        yield session
    finally:
        session.close()