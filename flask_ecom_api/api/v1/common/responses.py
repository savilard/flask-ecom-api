from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from flask import jsonify

from flask_ecom_api.app import db, marshmallow

ResponseType = Dict[str, List[Dict[str, Union[int, str]]]]  # noqa: WPS221


@dataclass
class ApiHttpResponse:
    """Http response attributes."""

    status: int
    message: Optional[str] = None
    detail: Optional[str] = None
    schema: Optional[marshmallow.SQLAlchemySchema] = None
    response_db_query: Optional[db.Model] = None

    def make_error_response(self) -> ResponseType:
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

    def make_success_response(self) -> ResponseType:
        """Return success response."""
        if self.schema:
            response = jsonify({'data': self.schema.dump(self.response_db_query)})
            response.status_code = self.status
            return response
        response = jsonify(
            {
                'data': [
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
