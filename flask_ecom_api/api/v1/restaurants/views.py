from http import HTTPStatus

from flask import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Restaurant  # type: ignore
from flask_ecom_api.api.v1.common.success_responses import make_success_response
from flask_ecom_api.api.v1.restaurants.schemas import restaurant_schema
from flask_ecom_api.app import db

restaurant_blueprint = Blueprint('restaurants', __name__, url_prefix='/api/v1')


@restaurant_blueprint.route('/restaurants', methods=['POST'])
@use_args(restaurant_schema)
def create_product(args):
    """Create new product."""
    new_restaurant = Restaurant(
        name=args.get('name'),
        address=args.get('address'),
        latitude=args.get('latitude'),
        longitude=args.get('longitude'),
        contact_phone=args.get('contact_phone'),
    )
    db.session.add(new_restaurant)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return make_success_response(
        schema=restaurant_schema,
        response_db_query=new_restaurant,
        status_code=HTTPStatus.CREATED,
    )
