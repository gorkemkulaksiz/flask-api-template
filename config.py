import os
from os.path import join, dirname

from dotenv import load_dotenv

_dotenv_path = join(dirname(__file__), '.env')
load_dotenv(_dotenv_path)

def _sqlalchemy_conn_string(username, password, host, db):
    return f"mysql+pymysql://{username}:{password}@{host}/{db}"


def get_config(env):
    if env == "development":
        config = "DevelopmentConfig"
    elif env == "testing":
        config = "TestingConfig"
    else:
        config = "ProductionConfig"

    return config


class _Config(object):
    DEBUG = False
    TESTING = False

    # flask-smorest
    API_TITLE = os.environ.get("API_TITLE")
    API_VERSION = os.environ.get("API_VERSION")
    OPENAPI_VERSION = os.environ.get("OPENAPI_VERSION")

    # JWT
    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = _sqlalchemy_conn_string(
        os.environ.get("DB_USERNAME"),
        os.environ.get("DB_PASSWORD"),
        os.environ.get("DB_HOST"),
        os.environ.get("DB_NAME")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(_Config):
    pass


class DevelopmentConfig(_Config):
    DEBUG = True


class TestingConfig(_Config):
    TESTING = True
