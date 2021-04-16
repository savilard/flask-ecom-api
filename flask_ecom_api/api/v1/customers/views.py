from http import HTTPStatus

from flask import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Customer, CustomerShippingAddress  # type: ignore
from flask_ecom_api.api.v1.common.custom_flask_jwt_decorators import (
    admin_required,
)
from flask_ecom_api.api.v1.common.responses import ApiHttpResponse
from flask_ecom_api.api.v1.customers.schemas import (
    customer_schema,
    customer_shipping_address,
    customers_schema,
)
from flask_ecom_api.app import db

customer_blueprint = Blueprint('customers', __name__, url_prefix='/api/v1')


@customer_blueprint.route('/customers', methods=['POST'])
@use_args(customer_schema)
@jwt_required()
def create_customer(args):
    """Create new customer."""
    new_customer = Customer(
        name=args.get('name'),
        date_of_birth=args.get('date_of_birth'),
        email=args.get('email'),
    )
    db.session.add(new_customer)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=customer_schema,
        response_db_query=new_customer,
        status=HTTPStatus.CREATED,
    ).make_success_response()


@customer_blueprint.route('/customers', methods=['GET'])
@jwt_required()
@admin_required()
def get_customers():
    """Gets all customers from db."""
    try:
        customers = Customer.query.all()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=customers_schema,
        response_db_query=customers,
        status=HTTPStatus.OK,
    ).make_success_response()


@customer_blueprint.route('/customers/shipping_address', methods=['POST'])
@use_args(customer_shipping_address)
@jwt_required()
def create_customer_shipping_address(args):
    """Create new customer shipping address."""
    new_shipping_address = CustomerShippingAddress(
        customer_id=args.get('customer_id'),
        first_name=args.get('first_name'),
        last_name=args.get('last_name'),
        phone_number=args.get('phone_number'),
        country=args.get('country'),
        city=args.get('city'),
        street=args.get('street'),
        house_number=args.get('house_number'),
        apartment_number=args.get('apartment_number'),
        postcode=args.get('postcode'),
        comment=args.get('comment'),
    )
    db.session.add(new_shipping_address)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=customer_shipping_address,
        response_db_query=new_shipping_address,
        status=HTTPStatus.CREATED,
    ).make_success_response()


@customer_blueprint.route('/customers/<int:customer_id>', methods=['GET'])
@jwt_required()
def customer_detail(customer_id):
    """Get customer detail."""
    try:
        customer = Customer.query.filter_by(id=customer_id).first()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return ApiHttpResponse(
        schema=customer_schema,
        response_db_query=customer,
        status=HTTPStatus.OK,
    ).make_success_response()
