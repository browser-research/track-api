from utils.load_scripts import load_collection
from flask import Flask

from routes.ping import ping_blueprint
from routes.demo import demo_blueprint
from routes.scripts import scripts_blueprint
from routes.data import data_blueprint

app = Flask(__name__)

# app.config.from_object('config.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')

# Routes registration
app.register_blueprint(ping_blueprint)
app.register_blueprint(demo_blueprint)
app.register_blueprint(scripts_blueprint)
app.register_blueprint(data_blueprint)

if __name__ == "__main__":
    app.run()
