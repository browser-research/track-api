from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

ENV = environ.get("ENV")
if ENV == "DEVELOPMENT":
    DEBUG = True

DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_PORT = environ.get("DATABASE_PORT")
DATABASE_NAME = environ.get("DATABASE_NAME")
DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASS = environ.get("DATABASE_PASS")

TRACK_HOSTNAME = environ.get("TRACK_HOSTNAME")
