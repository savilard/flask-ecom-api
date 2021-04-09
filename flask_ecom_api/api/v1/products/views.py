from flask import Blueprint, jsonify
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Product, ProductImage  # type: ignore
from flask_ecom_api.api.v1.common.error_responses import ErrorResponse
from flask_ecom_api.api.v1.products.schemas import (
    product_image_schema,
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
        response = ErrorResponse(
            status=500,  # noqa: WPS432
            message='Internal Server Error',
            detail='There was an internal server error',
        ).construct_error_response()
        return jsonify(response), 500

    response = {'data': products_schema.dump(all_products)}
    return jsonify(response), 200


@product_blueprint.route('/products', methods=['POST'])
@use_args(product_schema)
def create_product(args):
    """Create new product."""
    new_product_name = args.get('name')
    new_product = Product(
        name=new_product_name,
        description=args.get('description'),
        price=args.get('price'),
        published=args.get('published'),
    )
    db.session.add(new_product)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        response = ErrorResponse(
            status=500,  # noqa: WPS432
            message='Internal Server Error',
            detail=f'The product named "{new_product_name}" is not created',
        ).construct_error_response()
        return jsonify(response), 500

    response = {'data': product_schema.dump(new_product)}
    return jsonify(response), 201


@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Get product detail."""
    try:
        product = Product.query.filter_by(id=product_id).first()
    except SQLAlchemyError:
        response = ErrorResponse(
            status=500,  # noqa: WPS432
            message='Internal Server Error',
            detail='There was an internal server error',
        ).construct_error_response()
        return jsonify(response), 500

    if not product:
        response = ErrorResponse(
            status=404,  # noqa: WPS432
            message='Product not found',
            detail='The requested product could not be found',
        ).construct_error_response()
        return jsonify(response), 404

    response = {'data': product_schema.dump(product)}
    return jsonify(response), 200


@product_blueprint.route('/images', methods=['POST'])
@use_args(product_image_schema)
def create_product_image(args):
    """Create product image."""
    new_product_image = ProductImage(
        src=args.get('src'),
    )
    db.session.add(new_product_image)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        response = ErrorResponse(
            status=500,  # noqa: WPS432
            message='Internal Server Error',
            detail=f'The image with src "{new_product_image}" is not created',
        ).construct_error_response()
        return jsonify(response), 500

    response = {'data': product_image_schema.dump(new_product_image)}
    return jsonify(response), 201


@product_blueprint.errorhandler(422)  # noqa: WPS432
@product_blueprint.errorhandler(400)  # noqa: WPS432
def handle_error(err):
    """Return validation errors as JSON."""
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request.'])
    if headers:
        return jsonify({'errors': messages}), err.code, headers
    return jsonify({'errors': messages}), err.code
