from dataclasses import dataclass
from typing import Dict, List, Union

from flask import jsonify

from flask_ecom_api.app import db, marshmallow

ResponseType = Dict[str, List[Dict[str, Union[int, str]]]]  # noqa: WPS221


@dataclass
class BaseApi:
    """Base api response class."""

    status: int


@dataclass()
class ApiError(BaseApi):
    """Error response attribute."""

    message: str
    detail: str

    def response(self):
        """Return error response."""
        response = jsonify(
            {
                'errors': [
                    {
                        'status': self.status,
                        'message': self.message,
                        'detail': self.detail,
                    },
                ],
            },
        )
        response.status_code = self.status
        return response


@dataclass()
class ApiSuccess(BaseApi):
    """Success response attribute."""

    schema: marshmallow.SQLAlchemySchema
    response_db_query: db.Model

    def response(self):
        """Return success response."""
        response = jsonify({'data': self.schema.dump(self.response_db_query)})
        response.status_code = self.status
        return response
