
from flask import Blueprint
from flask_restful import Api

from find_it.auth.resources import Login, TokenRefresh

auth = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_api = Api(auth)

auth_api.add_resource(Login, '/token')
auth_api.add_resource(TokenRefresh, '/refresh')
