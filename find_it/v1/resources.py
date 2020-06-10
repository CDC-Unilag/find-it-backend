
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from . import v1, v1_api
from .schemas import UserCreationSchema, UserSchema, LeaderboardSchema
from ..utils.helpers import Helpers
from ..models import User
from ..core.permissions import admin_required


@v1.route('/', methods=['GET'])
def index():
    return Helpers.format_response(200)


class UserResource(Resource):
    method_decorators = {'get': [admin_required]}

    def get(self):
        all_users = User.query.order_by('id').all()
        schema_data = UserSchema().dump(all_users, many=True)
        return Helpers.format_response(200, data=schema_data)

    def post(self):
        data = request.get_json(force=True)
        schema = UserCreationSchema()
        try:
            new_user = schema.load(data)
        except ValidationError as e:
            return Helpers.format_response(400, error_detail=e.messages)
        return Helpers.format_response(201, data=new_user)


class LeaderboardResource(Resource):
    def get(self):
        order_by = request.args.get('order_by')
        if order_by not in ('points', 'submissions'):
            order_by = 'points'
        user_ranking = User.query.order_by(order_by).all()
        schema_data = LeaderboardSchema(many=True).dump(user_ranking)
        return Helpers.format_response(200, data=schema_data)


@v1.route('<path:invalid_path>')
def resource_not_found(invalid_path):
    return Helpers.format_response(
        404, error_detail='resource not found on this server'
    )


v1_api.add_resource(UserResource, '/user')
v1_api.add_resource(LeaderboardResource, '/leaderboard')
