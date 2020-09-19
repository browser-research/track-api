from datetime import datetime

from flask import request, json, Blueprint

data_blueprint = Blueprint('data', __name__,)


@data_blueprint.route('/data/push', methods=['POST'])
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

        print(json.dumps(data))
