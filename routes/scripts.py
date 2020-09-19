from utils.load_scripts import load_collection

from flask import Blueprint
scripts_blueprint = Blueprint('scripts', __name__,)

collection_content = load_collection()


@scripts_blueprint.route('/scripts/collection')
def get_script():
    return collection_content
