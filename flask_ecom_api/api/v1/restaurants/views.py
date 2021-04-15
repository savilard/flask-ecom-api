from http import HTTPStatus

from flask import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Restaurant, RestaurantProduct  # type: ignore
from flask_ecom_api.api.v1.common.responses import ApiHttpResponse
from flask_ecom_api.api.v1.restaurants.schemas import (
    restaurant_product_schema,
    restaurant_schema,
    restaurants_schema,
)
from flask_ecom_api.app import db

restaurant_blueprint = Blueprint('restaurants', __name__, url_prefix='/api/v1')


@restaurant_blueprint.route('/restaurants', methods=['POST'])
@use_args(restaurant_schema)
def create_restaurant(args):
    """Create new restaurant."""
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

    return ApiHttpResponse(
        schema=restaurant_schema,
        response_db_query=new_restaurant,
        status=HTTPStatus.CREATED,
    ).make_success_response()


@restaurant_blueprint.route('/restaurants/relationships/products', methods=['POST'])
@use_args(restaurant_product_schema)
def create_restaurant_and_product_relationship(args):
    """Creates new relationship between restaurant and product."""
    new_restaurant_and_product_relationship = RestaurantProduct(
        restaurant_id=args.get('restaurant_id'),
        product_id=args.get('product_id'),
        availability=args.get('availability'),
    )
    db.session.add(new_restaurant_and_product_relationship)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=restaurant_product_schema,
        response_db_query=new_restaurant_and_product_relationship,
        status=HTTPStatus.CREATED,
    ).make_success_response()


@restaurant_blueprint.route('/restaurants', methods=['GET'])
def get_all_restaurants():
    """Gets all restaurants from db."""
    try:
        all_restaurants = Restaurant.query.all()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=restaurants_schema,
        response_db_query=all_restaurants,
        status=HTTPStatus.OK,
    ).make_success_response()


@restaurant_blueprint.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def restaurant_detail(restaurant_id):
    """Get restaurant detail."""
    try:
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
    return ApiHttpResponse(
        schema=restaurant_schema,
        response_db_query=restaurant,
        status=HTTPStatus.OK,
    ).make_success_response()
