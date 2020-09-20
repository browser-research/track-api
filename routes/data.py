from datetime import datetime
import json

from flask import request, json, Blueprint, jsonify
from flask_cors import CORS

from db.mongodb import add_raw_record

data_blueprint = Blueprint('data', __name__,)
CORS(data_blueprint)


@data_blueprint.route('/data/push', methods=['POST', 'OPTIONS'])
def push_data():

    if request.method == "POST":

        headers = {
            "User-Agent": request.headers.get("User-Agent"),
            "Accept-Language": request.headers.get("Accept-Language")
        }
        request_data = {
            "ip": request.remote_addr,
            "HTTP_HOST": request.environ.get('HTTP_ORIGIN', 'default value')
        }
        data = {
            "timestamp": datetime.now().strftime("%d:%m:%Y %H:%M:%S"),
            **json.loads(request.get_data()),
            **request_data,
            **headers
        }

        # TODO: Uncomment before deployment
        # add_raw_record(json.dumps(data))

        return ("Browser data received"), 200

    return ("Unable to process your request"), 405
