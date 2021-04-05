from flask import Blueprint
from flask_restx import Api, Resource

product_blueprint = Blueprint('products', __name__)
api = Api(product_blueprint)


@api.route('/api/v1/products')
class ProductListAPI(Resource):
    """Product list API class."""

    def get(self):
        """Get method for ProductListAPI."""
        response = {
            'status': 'success',
            'message': 'list of products',
        }
        return response, 200


@api.route('/api/v1/products/<int:product_id>')
class ProductAPI(Resource):
    """Product API class."""

    def get(self, product_id):
        """Get method for ProductAPI."""
        response = {
            'status': 'success',
            'message': f'{product_id}',
        }
        return response, 200
