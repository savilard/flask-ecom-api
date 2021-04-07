import os

from flask import Flask
from flask_migrate import Migrate

from flask_ecom_api.api.v1.products.models import Ingredient, Product
from flask_ecom_api.api.v1.products.views import product_blueprint
from flask_ecom_api.app import admin, app, db

migrate = Migrate(compare_type=True)


def register_blueprints(current_app) -> None:
    """Register app blueprints."""
    current_app.register_blueprint(product_blueprint)


def create_app() -> Flask:
    """Create flask app."""
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
