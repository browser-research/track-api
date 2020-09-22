from decouple import config
from pymongo import MongoClient

DATABASE_HOST = config("DATABASE_HOST")
DATABASE_PORT = int(config("DATABASE_PORT"))
DATABASE_NAME = config("DATABASE_NAME")
DATABASE_USER = config("DATABASE_USER")
DATABASE_PASS = config("DATABASE_PASS")


def open_db_connection():
    client = MongoClient("mongodb://%s:%s@%s:%s/%s" %
                         (DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME))

    return client[DATABASE_NAME]


def add_raw_record(content):
    db = open_db_connection()

    return db.raw.insert_one(content).inserted_id
