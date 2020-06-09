
from . import main
from ..utils.helpers import Helpers


@main.app_errorhandler(404)
def resource_not_found(e):
    return Helpers.format_response(
        404, error_detail='resource not found on this server'
    )
