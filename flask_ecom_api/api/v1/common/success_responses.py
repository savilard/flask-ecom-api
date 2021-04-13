from flask import jsonify


def make_success_response(schema, response_db_query, status_code: int):
    """Returns success response.

    :param schema: Marshmallow schema
    :param response_db_query: response from the database to the request
    :param status_code: response status code
    """
    return jsonify({'data': schema.dump(response_db_query)}), status_code
