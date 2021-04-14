from http import HTTPStatus

from flask import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Customer  # type: ignore
from flask_ecom_api.api.v1.common.success_responses import make_success_response
from flask_ecom_api.api.v1.customers.schemas import (
    customer_schema,
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
