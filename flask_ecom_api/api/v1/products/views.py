from http import HTTPStatus

from flask import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Product, ProductImage  # type: ignore
from flask_ecom_api.api.v1.common.responses import ApiHttpResponse
from flask_ecom_api.api.v1.products.schemas import (
    product_image_schema,
    product_schema,
    products_schema,
)
from flask_ecom_api.app import db

product_blueprint = Blueprint('products', __name__, url_prefix='/api/v1')


@product_blueprint.route('/products', methods=['GET'])
@jwt_required()
def get_all_products():
    """Gets all products from db."""
    try:
        all_products = Product.query.all()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=products_schema,
        response_db_query=all_products,
        status=HTTPStatus.OK,
    ).make_success_response()


@product_blueprint.route('/products', methods=['POST'])
@use_args(product_schema)
@jwt_required()
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
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=product_schema,
        response_db_query=new_product,
        status=HTTPStatus.CREATED,
    ).make_success_response()


@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
def product_detail(product_id):
    """Get product detail."""
    try:
        product = Product.query.filter_by(id=product_id).first()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
    return ApiHttpResponse(
        schema=product_schema,
        response_db_query=product,
        status=HTTPStatus.OK,
    ).make_success_response()


@product_blueprint.route('/images', methods=['POST'])
@use_args(product_image_schema)
@jwt_required()
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
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=product_image_schema,
        response_db_query=new_product_image,
        status=HTTPStatus.CREATED,
    ).make_success_response()
