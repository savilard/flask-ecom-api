from flask import Blueprint, jsonify
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Product, ProductImage  # type: ignore
from flask_ecom_api.api.v1.common.error_responses import make_error_response
from flask_ecom_api.api.v1.common.success_responses import make_success_response
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
        return make_error_response(status_code=500)

    return make_success_response(
        schema=products_schema,
        response_db_query=all_products,
        status_code=200,
    )


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
        return make_error_response(status_code=500)

    return make_success_response(
        schema=product_schema,
        response_db_query=new_product,
        status_code=201,
    )


@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Get product detail."""
    try:
        product = Product.query.filter_by(id=product_id).first()
    except SQLAlchemyError:
        return make_error_response(status_code=500)

    if not product:
        return make_error_response(
            status_code=404,
            message='Product not found',
            detail=f'The product with id={product_id} could not be found',
        )

    return make_success_response(schema=product_schema, response_db_query=product, status_code=200)


@product_blueprint.route('/images', methods=['POST'])
@use_args(product_image_schema)
def create_product_image(args):
    """Create product image."""
    new_product_image = ProductImage(
        src=args.get('src'),
        product_id=args.get('product_id'),
    )
    db.session.add(new_product_image)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        return make_error_response(status_code=500)

    return make_success_response(
        schema=product_image_schema,
        response_db_query=new_product_image,
        status_code=201,
    )


@product_blueprint.errorhandler(422)
@product_blueprint.errorhandler(400)
def handle_error(err):
    """Return validation errors as JSON."""
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request.'])
    if headers:
        return jsonify({'errors': messages}), err.code, headers
    return jsonify({'errors': messages}), err.code
