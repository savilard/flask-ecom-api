import uuid
from dataclasses import dataclass
from typing import Dict, Optional, Union

from flask import jsonify


@dataclass
class HttpError:
    """Http error dataclass."""

    status_code: int
    message: Optional[str]
    detail: Optional[str]
    request_id: str = uuid.uuid4().hex

    def to_dict(self) -> Dict[str, Union[int, str, None]]:
        """Convert HttpError to dict."""
        return {
            'status': self.status_code,
            'message': self.message,
            'detail': self.detail,
            'request_id': self.request_id,
        }


def make_error_response(
    status_code: int,
    message: Optional[str] = None,
    detail: Optional[str] = None,
):
    """Returns an error response.

    If status code = 500, message and detailed message do not need to be transmitted.

    :param status_code: error status code
    :param message: error text
    :param detail: error detail text
    :return: error response and status code
    """
    errors = {
        500: HttpError(
            status_code=500,  # noqa: WPS432
            message='Internal Server Error',
            detail='There was an internal server error',
        ).to_dict(),
    }

    error = errors.get(
        status_code,
        HttpError(
            status_code=status_code,
            message=message,
            detail=detail,
        ).to_dict(),
    )

    return jsonify({'errors': [error]}), error['status']
