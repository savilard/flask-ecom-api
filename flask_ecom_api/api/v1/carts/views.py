from http import HTTPStatus

from flask import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import Cart  # type: ignore
from flask_ecom_api.api.v1.carts.schemas import cart_schema
from flask_ecom_api.api.v1.common.success_responses import make_success_response
from flask_ecom_api.app import db

cart_blueprint = Blueprint('carts', __name__, url_prefix='/api/v1')


@cart_blueprint.route('/carts', methods=['POST'])
@use_args(cart_schema)
def create_cart(args):
    """Create new cart."""
    new_cart = Cart(
        reference=args.get('reference'),
    )
    db.session.add(new_cart)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return make_success_response(
        schema=cart_schema,
        response_db_query=new_cart,
        status_code=HTTPStatus.CREATED,
    )
