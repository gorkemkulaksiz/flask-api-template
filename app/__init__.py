from flask import Flask
from flask_smorest import Api

from config import get_config
from app.database import db, migrate

def create_app(config="development"):
    app = Flask(__name__)

    app.config.from_object(f"config.{get_config(config)}")

    db.init_app(app)
    migrate.init_app(app, db)

    # This is a good place to add app-wide request hooks

    api = Api(app)

    # Register blueprints here:
    # api.register_blueprint(model_blueprint)

    # Importing models here so that flask-migrate can see them
    from app import models

    return app

