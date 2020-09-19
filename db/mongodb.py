from decouple import config

DATABASE_HOST = config("DATABASE_HOST")
DATABASE_USER = config("DATABASE_USER")
DATABASE_PASS = config("DATABASE_PASS")

db_connection = False

def open_db_connection():
    print(DATABASE_HOST, DATABASE_USER, DATABASE_PASS)
