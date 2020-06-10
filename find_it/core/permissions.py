from functools import wraps

from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims

from find_it.utils.helpers import Helpers


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims.get('admin'):
            return Helpers.format_response(403)
        else:
            return fn(*args, **kwargs)
    return wrapper
