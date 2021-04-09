from dataclasses import dataclass


@dataclass
class ErrorResponse:  # noqa: WPS306
    """Error response dataclass."""

    status: int
    message: str
    detail: str

    def construct_error_response(self):
        """Return error response in dict.

        :return: error response
        :type: Dict[str, List[Dict[str, Union[int, str]]

        """
        return {
            'errors': [
                {
                    'status': self.status,
                    'message': self.message,
                    'detail': self.detail,
                },
            ],
        }
