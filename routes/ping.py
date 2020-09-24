from flask import Blueprint

ping_blueprint = Blueprint("ping", __name__,)


@ping_blueprint.route("/ping")
def hello():
    return "Application is running"
