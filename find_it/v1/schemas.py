import re

from marshmallow import (
    fields, validates, validates_schema, ValidationError, post_load
)

from find_it import ma, db
from ..models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    points = ma.auto_field()
    submissions = ma.auto_field()


class UserCreationSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)

    @validates('username')
    def validate_username(self, value):
        value = value.strip()
        if not 4 < len(value) < 64:
            raise ValidationError(
                'username length should be greater than 4 and less than 64'
            )
        exists = User.query.filter(User.username.ilike(value)).first()
        if exists:
            raise ValidationError(
                'user with this username already exists'
            )
        username_pattern = re.compile(r'^[a-zA-Z0-9_]+$')
        if not username_pattern.match(value):
            raise ValidationError(
                'username can contain underscores, numbers and letters only'
            )
        if set(value) == {'_'}:
            raise ValidationError(
                'username can not be only underscores'
            )
        if value in User.DISALLOWED_USERNAMES:
            raise ValidationError(
                'username not allowed, choose another'
            )

    @validates_schema
    def validate(self, data, **kwargs):
        if data['password'] != data['confirm_password']:
            raise ValidationError('passwords do not match')

    @post_load
    def make_user(self, data, **kwargs):
        user = User(data['username'])
        user.password = data['password']
        db.session.add(user)
        db.session.commit()
        new_user_schema = UserSchema().dump(user)
        return new_user_schema


class LeaderboardSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field()
    points = ma.auto_field()
    submissions = ma.auto_field()
