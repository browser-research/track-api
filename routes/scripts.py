from flask import Blueprint, current_app, make_response

scripts_blueprint = Blueprint("scripts", __name__,)


@scripts_blueprint.route("/scripts/collection")
def collection():
    response = make_response(current_app.collection_content)
    response.mimetype = "application/javascript"
    return response
