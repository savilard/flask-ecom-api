from http import HTTPStatus

from flask import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Customer, CustomerShippingAddress  # type: ignore
from flask_ecom_api.api.v1.common.success_responses import make_success_response
from flask_ecom_api.api.v1.customers.schemas import (
    customer_schema,
    customer_shipping_address,
    customers_schema,
)
from flask_ecom_api.app import db

customer_blueprint = Blueprint('customers', __name__, url_prefix='/api/v1')


@customer_blueprint.route('/customers', methods=['POST'])
@use_args(customer_schema)
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

    return make_success_response(
        schema=customer_schema,
        response_db_query=new_customer,
        status_code=HTTPStatus.CREATED,
    )


@customer_blueprint.route('/customers', methods=['GET'])
def get_customers():
    """Gets all customers from db."""
    try:
        customers = Customer.query.all()
    except SQLAlchemyError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return make_success_response(
        schema=customers_schema,
        response_db_query=customers,
        status_code=HTTPStatus.OK,
    )


@customer_blueprint.route('/customers/shipping_address', methods=['POST'])
@use_args(customer_shipping_address)
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

    return make_success_response(
        schema=customer_shipping_address,
        response_db_query=new_shipping_address,
        status_code=HTTPStatus.CREATED,
    )


@customer_blueprint.route('/customers/<int:customer_id>', methods=['GET'])
def customer_detail(customer_id):
    """Get customer detail."""
    try:
        customer = Customer.query.filter_by(id=customer_id).first()
    except SQLAlchemyError:
        abort(500)

    return make_success_response(
        schema=customer_schema,
        response_db_query=customer,
        status_code=HTTPStatus.OK,
    )
