from flask import Blueprint
from flask_restx import Api, Resource

product_blueprint = Blueprint('product', __name__)
api = Api(product_blueprint)


@api.route('/api/v1/products', endpoint='products')
class ProductListAPI(Resource):
    def get(self):
        response = {
            'status': 'success',
            'message': 'list of products',
        }
        return response, 200

    def post(self):
        pass


@api.route('/api/v1/products/<int:product_id>', endpoint='product')
class ProductAPI(Resource):
    def get(self, product_id):
        response = {
            'status': 'success',
            'message': f'{product_id}',
        }
        return response, 200

    def put(self):
        pass

    def delete(self):
        pass
