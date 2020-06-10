
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

from config import config

app = Flask(__name__)

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()


def create_app(config_environment):
    app = Flask(__name__)
    config_object = config.get(config_environment, 'default')
    app.config.from_object(config_object)
    config_object.init_app(app)

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    from find_it.v1 import v1 as v1_blueprint
    from find_it.auth import auth as auth_blueprint
    app.register_blueprint(v1_blueprint)
    app.register_blueprint(auth_blueprint)

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        from find_it.models import User
        user = User.query.get(identity)
        if user and user.is_admin:
            return {'admin': True}
    return app
