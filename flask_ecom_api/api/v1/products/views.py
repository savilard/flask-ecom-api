from flask import Blueprint, jsonify
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Product  # type: ignore
from flask_ecom_api.api.v1.products.schemas import (
    product_schema,
    products_schema,
)
from flask_ecom_api.app import db

product_blueprint = Blueprint('products', __name__, url_prefix='/api/v1')


@product_blueprint.route('/products', methods=['GET'])
def get_all_products():
    """Gets all products from db."""
    try:
        all_products = Product.query.all()
    except SQLAlchemyError:
        response = {
            'errors': [
                {
                    'status': 500,
                    'message': 'Internal Server Error',
                    'detail': 'There was an internal server error',
                },
            ],
        }
        return jsonify(response), 500

    response = {'data': products_schema.dump(all_products)}
    return jsonify(response), 200


@product_blueprint.route('/products', methods=['POST'])
@use_args(product_schema)
def create_product(args):
    """Create new product."""
    new_product = Product(
        name=args.get('name'),
        description=args.get('description'),
        price=args.get('price'),
        published=args.get('published'),
    )
    db.session.add(new_product)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        response = {
            'errors': [
                {
                    'status': 500,
                    'message': 'Internal Server Error',
                    'detail': 'There was an internal server error',
                },
            ],
        }
        return jsonify(response), 500

    response = {'data': product_schema.dump(new_product)}
    return jsonify(response), 201


@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Get product detail."""
    try:
        product = Product.query.filter_by(id=product_id).first()
    except SQLAlchemyError:
        response = {
            'errors': [
                {
                    'status': 500,
                    'message': 'Internal Server Error',
                    'detail': 'There was an internal server error',
                },
            ],
        }
        return jsonify(response), 500

    if not product:
        response = {
            'error': [
                {
                    'status': 404,
                    'detail': 'The requested product could not be found',
                    'message': 'Product not found',
                },
            ],
        }
        return jsonify(response), 404

    response = {'data': product_schema.dump(product)}
    return jsonify(response), 200


@product_blueprint.errorhandler(422)  # noqa: WPS432
@product_blueprint.errorhandler(400)  # noqa: WPS432
def handle_error(err):
    """Return validation errors as JSON."""
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request.'])
    if headers:
        return jsonify({'errors': messages}), err.code, headers
    return jsonify({'errors': messages}), err.code
