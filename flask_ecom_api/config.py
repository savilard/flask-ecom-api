import datetime
import os


class BaseConfig:
    """Base configuration."""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_cool_secret_key')
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'connect_timeout': 500,
        },
    }
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(
        hours=int(os.environ.get('JWT_TOKEN_LIFETIME', 5)),
    )


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
