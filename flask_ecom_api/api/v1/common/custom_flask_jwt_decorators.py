from functools import wraps
from http import HTTPStatus

from flask_jwt_extended import get_jwt, verify_jwt_in_request

from flask_ecom_api.api.v1.common.responses import ApiError


def admin_required():
    """Checking for the presence of the admin role for the user."""
    def wrapper(fn):
        """Decorator wrapper."""
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get('is_administrator'):
                return fn(*args, **kwargs)
            return ApiError(
                status=HTTPStatus.FORBIDDEN,
                message='Only admin',
                detail='Insufficient rights to work with this endpoint.',
            ).response()

        return decorator

    return wrapper
