from os import getenv

from dotenv import load_dotenv

load_dotenv()

FIEF_DOMAIN = "https://" + getenv("FIEF_DOMAIN")
FIEF_CLIENT_ID = getenv("FIEF_CLIENT_ID")
FIEF_CLIENT_SECRET = getenv("FIEF_CLIENT_SECRET")
SECRET = getenv("SECRET")

PGHOST = getenv("DATABASE_HOST")
PGPORT = getenv("DATABASE_PORT")
PGUSER = getenv("DATABASE_USER")
PGPASSWORD = getenv("DATABASE_PASSWORD")
PGDATABASE = getenv("DATABASE_NAME")
