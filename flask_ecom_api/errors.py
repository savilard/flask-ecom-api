from dataclasses import dataclass
from http import HTTPStatus
from typing import Dict, List, Union

from flask import jsonify

ErrorResponseType = Dict[str, List[Dict[str, Union[int, str]]]]  # noqa: WPS221


@dataclass
class HttpError:
    """Http error attributes."""

    status: int
    message: str
    detail: str

    def make_error_response(self) -> ErrorResponseType:
        """Return error response."""
        return {
            'errors': [
                {
                    'status': self.status,
                    'message': self.message,
                    'detail': self.detail,
                },
            ],
        }


def handle_not_found_error(err):
    """404 error response."""
    response = HttpError(
        status=HTTPStatus.NOT_FOUND,
        message='Not found',
        detail='The requested URL was not found on the server',
    ).make_error_response()
    return jsonify(response), HTTPStatus.NOT_FOUND


def handle_internal_server_error(err):
    """500 error handler."""
    response = HttpError(
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
        message='Internal Server Error',
        detail='There was an internal server error',
    ).make_error_response()

    return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR


def handle_validation_errors(err):
    """Return validation errors as JSON."""
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request.'])
    if headers:
        return jsonify({'errors': messages}), err.code, headers
    return jsonify({'errors': messages}), err.code
