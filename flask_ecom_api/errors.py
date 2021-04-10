from flask import jsonify


def not_found_error(err):
    """404 error response."""
    response = {
        'errors': [
            {
                'status': 404,
                'message': 'not found',
                'detail': 'The requested URL was not found on the server',
            },
        ],
    }
    return jsonify(response), 404


def internal_server_error(err):
    """500 error handler."""
    response = {
        'errors': [
            {
                'status': 500,
                'message': 'Internal Server Error',
                'detail': 'There was an internal server error',
            },
        ],
    }

    return jsonify(response), 500
