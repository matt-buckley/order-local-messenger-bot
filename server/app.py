from flask import request, jsonify, url_for, Flask, redirect
from flask_cors import CORS


app = Flask(__name__)
# TODO: Limit CORS to same domain
CORS(app)


@app.route('/test', methods=['GET'])
def test():
    return "I'm a teapot!", 418


