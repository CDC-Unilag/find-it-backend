
from . import v1
from ..utils.helpers import Helpers


@v1.app_errorhandler(401)
def unauthorized(e):
    return Helpers.format_response(
        404, error_detail='you are not permitted to access this resource'
    )
