from http import HTTPStatus

from flask import jsonify

from flask_ecom_api.api.v1.common.responses import ApiError


def handle_not_found_error(err):
    """404 error response."""
    return ApiError(
        status=HTTPStatus.NOT_FOUND,
        message='Not found',
        detail='The requested URL was not found on the server',
    ).response()


def handle_internal_server_error(err):
    """500 error handler."""
    return ApiError(
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
        message='Internal Server Error',
        detail='There was an internal server error',
    ).response()


def handle_validation_errors(err):
    """Return validation errors as JSON."""
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request.'])
    if headers:
        return jsonify({'errors': messages}), err.code, headers
    return jsonify({'errors': messages}), err.code
