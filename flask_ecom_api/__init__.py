from flask import Blueprint, Flask
from flask_restful import Api

from flask_ecom_api.v1.endpoints.products import ProductAPI, ProductListAPI

app = Flask(__name__)
app.config.from_object('flask_ecom_api.config.DevelopmentConfig')

api_blueprint = Blueprint(app, __name__)

api = Api(api_blueprint)

api.add_resource(ProductListAPI, '/api/v1/products', endpoint='products')
api.add_resource(ProductAPI, '/api/v1/products/<int:product_id>', endpoint='product')

app.register_blueprint(api_blueprint)
