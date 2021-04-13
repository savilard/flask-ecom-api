import os

from flask import Flask
from flask_migrate import Migrate

from flask_ecom_api.api.v1.carts.models import Cart, CartProduct
from flask_ecom_api.api.v1.carts.views import cart_blueprint
from flask_ecom_api.api.v1.products.models import (
    Category,
    Ingredient,
    Product,
    ProductImage,
)
from flask_ecom_api.api.v1.products.views import product_blueprint
from flask_ecom_api.app import admin, app, db
from flask_ecom_api.errors import (
    handle_internal_server_error,
    handle_not_found_error,
    handle_validation_errors,
)

migrate = Migrate(compare_type=True)


def register_blueprints(current_app) -> None:
    """Register app blueprints."""
    current_app.register_blueprint(product_blueprint)
    current_app.register_blueprint(cart_blueprint)


def create_app() -> Flask:
    """Create flask app."""
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    app.register_error_handler(400, handle_validation_errors)
    app.register_error_handler(404, handle_not_found_error)
    app.register_error_handler(422, handle_validation_errors)
    app.register_error_handler(500, handle_internal_server_error)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
