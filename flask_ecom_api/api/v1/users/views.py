from http import HTTPStatus

from flask import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import User  # type: ignore
from flask_ecom_api.api.v1.users.schemas import user_schema
from flask_ecom_api.app import db
from flask_ecom_api.errors import HttpError

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_blueprint.route('/register', methods=['POST'])
@use_args(user_schema)
def register_user(args):
    """Register new user."""
    user_email = args.get('email')
    user = User.query.filter(User.email == user_email).first()
    if user:
        return HttpError(
            status=HTTPStatus.BAD_REQUEST,
            message='User exists',
            detail='Sorry. That user already exists.',
        ).make_error_response()

    new_user = User(
        username=args.get('username'),
        email=user_email,
    )
    new_user.set_password(args.get('password'))
    db.session.add(new_user)
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return HttpError(
        status=HTTPStatus.CREATED,
        message='Successfully registered',
        detail=f'User with {user_email} successfully registered',
    ).make_error_response()
