from datetime import datetime
import json

from flask import request, json, Blueprint, jsonify, current_app
from flask_cors import CORS, cross_origin

data_blueprint = Blueprint("data", __name__,)
CORS(data_blueprint, supports_credentials=True)


@data_blueprint.route("/data/push", methods=["POST", "OPTIONS"])
@cross_origin()
def data_push():

    if request.method == "POST":

        if request.environ.get("HTTP_X_FORWARDED_FOR") is None:
            ip = request.environ["REMOTE_ADDR"]
        else:
            ip = request.environ["HTTP_X_FORWARDED_FOR"]

        if "," in ip and ip is not None:
            ip = ip.split(",")[0]

        headers = {
            "HTTP_User-Agent": request.headers.get("User-Agent"),
            "HTTP_Accept-Language": request.headers.get("Accept-Language")
        }
        request_data = {
            "HTTP_REMOTE_ADDR": ip,
            "HTTP_ORIGIN": request.environ.get("HTTP_ORIGIN", "default value")
        }
        data = {
            "timestamp": datetime.now().strftime("%d:%m:%Y %H:%M:%S"),
            **json.loads(request.get_data()),
            **request_data,
            **headers
        }

        if current_app.config["ENV"] == "DEVELOPMENT":
            # Push browser data into console instead of adding to database
            print(data)
        else:
            current_app.mongo_client.insert_one("raw", data)

        return ("Browser data received"), 200

    return ("Unable to process your request"), 405
