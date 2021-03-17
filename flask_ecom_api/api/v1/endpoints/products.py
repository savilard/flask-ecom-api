from flask import Blueprint
from flask_restful import Api, Resource

product_blueprint = Blueprint('product', __name__)
api = Api(product_blueprint)


class ProductListAPI(Resource):
    def get(self):
        response = {
            'status': 'success',
            'message': 'list of products',
        }
        return response, 200

    def post(self):
        pass


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


api.add_resource(ProductListAPI, '/api/v1/products', endpoint='products')
api.add_resource(ProductAPI, '/api/v1/products/<int:product_id>', endpoint='product')
