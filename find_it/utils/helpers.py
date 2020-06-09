
from flask import jsonify


class Helpers:
    @staticmethod
    def remove_empty_keys(data):
        new_data = {}
        for key, value in data.items():
            if value is not None:
                new_data[key] = value
        return new_data

    @staticmethod
    def format_response(code, data=None, error_detail=None):
        if error_detail and data:
            raise Exception(
                'Improperly configured: cant have both'
                ' data and error detail specified'
            )

        responses = {
            200: 'OK',
            201: 'created',
            404: 'not found',
        }
        response_obj = {
            'status': responses[code],
            'status_code': code,
        }
        if data:
            response_obj.update(data=data)
        elif error_detail:
            response_obj.update(error_detail=error_detail)
        return jsonify(response_obj), code
