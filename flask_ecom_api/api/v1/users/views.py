from http import HTTPStatus

from flask import Blueprint, abort, jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError
from webargs.flaskparser import use_args

from flask_ecom_api import User  # type: ignore
from flask_ecom_api.api.v1.common.responses import ApiHttpResponse
from flask_ecom_api.api.v1.users.schemas import user_schema
from flask_ecom_api.app import db

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_blueprint.route('/register', methods=['POST'])
@use_args(user_schema)
def register_user(args):
    """Register new user."""
    user_email = args.get('email')
    user = User.query.filter(User.email == user_email).first()
    if user:
        return ApiHttpResponse(
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

    return ApiHttpResponse(
        status=HTTPStatus.CREATED,
        message='Successfully registered',
        detail=f'User with {user_email} successfully registered',
    ).make_success_response()


@auth_blueprint.route('/access_token', methods=['POST'])
@use_args(user_schema)
def create_client_access_token(args):
    """Create client access token."""
    user_email = args.get('email')
    password = args.get('password')
    user = User.query.filter_by(email=user_email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user_email)
        return jsonify(access_token=access_token), HTTPStatus.CREATED

    return ApiHttpResponse(
        status=HTTPStatus.UNAUTHORIZED,
        message='Login failed',
        detail='Bad username or password',
    ).make_error_response()
