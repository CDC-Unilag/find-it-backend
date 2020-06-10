
from flask import current_app, request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity
)
from marshmallow import ValidationError

from find_it.utils.helpers import Helpers
from find_it.auth.schemas import UserLoginSchema


class Login(Resource):
    def post(self):
        data = request.get_json(force=True)
        schema = UserLoginSchema()
        try:
            user = schema.load(data)
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'expires_in': int(
                    current_app.config['JWT_ACCESS_TOKEN_EXPIRES']
                    .total_seconds()
                )
            }, 200
        except ValidationError as e:
            return Helpers.format_response(
                401,
                error_detail=e.messages
            )


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {
            'access_token': new_token
        }, 200
