from flask import Flask, jsonify, request, abort
from inference import process_request


APP = Flask(__name__)


@APP.route('/prediction', methods=['POST'])
def prediction():
    '''
    Handles the call from the client.
    '''
    if request.is_json:
        content = request.get_json()
    else:
        abort(404)
    return jsonify(process_request(content))
    # if request.form is not None:
    #     request.get_data()
    #     # print(type(request))
    #     print(request.json)
    #     result = process_request(request)
    #     print(result)
    #     return jsonify(process_request(request))


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
