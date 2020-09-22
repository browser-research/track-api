from datetime import datetime
import json

from flask import request, json, Blueprint, jsonify, current_app
from flask_cors import CORS

from db.mongodb import add_raw_record

data_blueprint = Blueprint('data', __name__,)
CORS(data_blueprint)


@data_blueprint.route('/data/push', methods=['POST', 'OPTIONS'])
def data_push():

    if request.method == "POST":

        headers = {
            "HTTP_User-Agent": request.headers.get("User-Agent"),
            "HTTP_Accept-Language": request.headers.get("Accept-Language")
        }
        request_data = {
            "HTTP_REMOTE_ADDR": request.remote_addr,
            "HTTP_ORIGIN": request.environ.get('HTTP_ORIGIN', 'default value')
        }
        data = {
            "timestamp": datetime.now().strftime("%d:%m:%Y %H:%M:%S"),
            **json.loads(request.get_data()),
            **request_data,
            **headers
        }

        if current_app.config['DEVELOPMENT']:
            # Push browser data into console instead of adding to databse
            print(data)
        else:
            # Add data to dev/production database
            add_raw_record(data)

        return ("Browser data received"), 200

    return ("Unable to process your request"), 405
