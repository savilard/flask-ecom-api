from flask import Blueprint, jsonify

from flask_ecom_api import Product  # type: ignore
from flask_ecom_api.api.v1.products.schemas import (
    product_schema,
    products_schema,
)

product_blueprint = Blueprint('products', __name__)


@product_blueprint.route('/products', methods=['GET'])
def products():
    """Gets all products from db."""
    all_products = Product.query.all()
    output = products_schema.dump(all_products)
    return jsonify({'data': output}), 200


@product_blueprint.route('/products/<product_id>', methods=['GET'])
def product_detail(product_id):
    """Get product detail."""
    product = Product.query.get(product_id)
    output = product_schema.dump(product)
    return jsonify({'data': output}), 200
