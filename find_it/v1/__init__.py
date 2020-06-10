
from flask import Blueprint
from flask_restful import Api


v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
v1_api = Api(v1)

from . import resources, errors
