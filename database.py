from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import PGUSER, PGHOST, PGDATABASE, PGPASSWORD, PGPORT

connection_string = URL.create(
    "postgresql",
    username=PGUSER,
    password=PGPASSWORD,
    host=PGHOST,
    port=PGPORT,
    database=PGDATABASE
)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = get_db()
Base = declarative_base()
