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
