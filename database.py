from os import getenv

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

connection_string = URL.create(
    "postgresql",
    username=getenv("PGUSER"),
    password=getenv("PGPASSWORD"),
    host=getenv("PGHOST"),
    database=getenv("PGDATABASE")
)

engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
