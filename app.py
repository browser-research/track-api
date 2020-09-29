from dotenv import load_dotenv
from flask import Flask

from utils.load_scripts import load_collection
from models.mongodb import MongoSession

from routes.ping import ping_blueprint
from routes.demo import demo_blueprint
from routes.scripts import scripts_blueprint
from routes.data import data_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Routes registration
app.register_blueprint(ping_blueprint)
app.register_blueprint(demo_blueprint)
app.register_blueprint(scripts_blueprint)
app.register_blueprint(data_blueprint)

# Setting some global vars
app.collection_content = load_collection(
    app.config["TRACK_HOSTNAME"], app.config["ENV"])

app.mongo_client = MongoSession(app.config["DATABASE_USER"], app.config["DATABASE_PASS"],
                                app.config["DATABASE_HOST"], app.config["DATABASE_PORT"], app.config["DATABASE_NAME"])

if __name__ == "__main__":
    app.run()
