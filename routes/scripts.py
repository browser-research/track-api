from flask import Blueprint, current_app

scripts_blueprint = Blueprint("scripts", __name__,)


@scripts_blueprint.route("/scripts/collection")
def get_script():
    return current_app.collection_content
