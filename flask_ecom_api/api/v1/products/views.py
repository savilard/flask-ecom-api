from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args

from flask_ecom_api import Product  # type: ignore
from flask_ecom_api.api.v1.products.schemas import (
    product_schema,
    products_schema,
)
from flask_ecom_api.app import db

product_blueprint = Blueprint('products', __name__, url_prefix='/api/v1')

product_args = {
    'name': fields.Str(required=True),  # type: ignore
    'description': fields.Str(),  # type: ignore
    'price': fields.Decimal(),  # type: ignore
    'published': fields.Bool(),  # type: ignore
}


@product_blueprint.route('/products', methods=['GET'])
def get_all_products():
    """Gets all products from db."""
    all_products = Product.query.all()
    output = products_schema.dump(all_products)
    return jsonify({'data': output}), 200


@product_blueprint.route('/products', methods=['POST'])
@use_args(product_args)
def create_product(args):
    """Create new product."""
    new_product = Product(
        name=args.get('name'),
        description=args.get('description'),
        price=args.get('price'),
        published=args.get('published'),
    )
    db.session.add(new_product)
    db.session.commit()
    output = product_schema.dump(new_product)
    return jsonify({'data': output}), 201


@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Get product detail."""
    product = Product.query.get(product_id)
    output = product_schema.dump(product)
    return jsonify({'data': output}), 200
