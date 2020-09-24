from flask import current_app

from pymongo import MongoClient


class MongoSession:
    def __init__(self, user, passwd, host, port, db_name):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.db_name = db_name

        self.connection_string = "mongodb://{}:{}@{}:{}/{}".format(
            self.user, self.passwd, self.host, self.port, self.db_name)

        self.client = MongoClient(self.connection_string)

    def insert_one(self, collection, content):
        with self.client:
            database = self.client[self.db_name]
            return database[collection].insert_one(content).inserted_id
