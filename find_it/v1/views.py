
from . import v1
from ..utils.helpers import Helpers


@v1.route('/', methods=['GET'])
def index():
    return Helpers.format_response(200)


@v1.route('<path:invalid_path>')
def resource_not_found(invalid_path):
    return Helpers.format_response(
        404, error_detail='resource not found on this server'
    )
