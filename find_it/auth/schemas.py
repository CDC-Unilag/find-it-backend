
from marshmallow import fields, validates_schema, ValidationError, post_load

from find_it import ma
from ..models import User


class UserLoginSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    @validates_schema
    def validate(self, data, **kwargs):
        username = data['username']
        self.user = User.query.filter(User.username.ilike(username)).first()
        if not self.user and self.user.verify_password(data['password']):
            raise ValidationError('invalid credentials')

    @post_load
    def get_user_obj(self, data, **kwargs):
        return self.user
