from flask import Blueprint, jsonify

from flask_ecom_api import Product  # type: ignore
from flask_ecom_api.api.v1.products.schemas import products_schema

product_blueprint = Blueprint('products', __name__)


@product_blueprint.route('/products', methods=['GET'])
def products():
    """Gets all products from db."""
    all_products = Product.query.all()
    return jsonify({'data': products_schema.dump(all_products)}), 200
