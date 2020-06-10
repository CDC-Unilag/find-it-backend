import os
from datetime import timedelta

from dotenv import load_dotenv


load_dotenv('dev.env')


class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///findit.db'


class ProductionConfig(Config):
    ...


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///findit_test.db'


config = {
 'development': DevelopmentConfig,
 'production': ProductionConfig,
 'testing': TestingConfig,
 'default': DevelopmentConfig
}
