
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)

db = SQLAlchemy()


def create_app(config_environment):
    app = Flask(__name__)
    config_object = config.get(config_environment, 'default')
    app.config.from_object(config_object)
    config_object.init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
