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
    API_TITLE = ""
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"

    # JWT
    SECRET_KEY = ""

    DB_NAME = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_HOST = ""

    SQLALCHEMY_DATABASE_URI = _sqlalchemy_conn_string(
        DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(_Config):
    pass


class DevelopmentConfig(_Config):
    DEBUG = True


class TestingConfig(_Config):
    TESTING = True
