from flask import jsonify, make_response


def custom_response(status_code, message):
    response =  make_response(jsonify({
        "status": status_code,
        "message": message
    }), status_code)
    return response