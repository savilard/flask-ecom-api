from flask_restful import Resource


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
