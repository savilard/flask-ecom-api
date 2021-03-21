import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_ecom_api.api.v1.products.views import product_blueprint

db = SQLAlchemy()


def register_blueprints(app) -> None:
    """Register app blueprints."""
    app.register_blueprint(product_blueprint)


def create_app() -> Flask:
    """Create flask app."""
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    register_blueprints(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
