from configparser import ConfigParser
from flask import request, jsonify, url_for, Flask, redirect
from flask_cors import CORS
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
# TODO: Limit CORS to same domain
CORS(app)

parser = ConfigParser()
parser.read('setup.conf')
VERIFY = parser.get('server', 'verify')
if not VERIFY:
    raise ValueError('Programmer error: You need to specify a verification code in setup.conf...')

@app.route('/test', methods=['GET'])
def test():
    return "I'm a teapot!", 418


@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    """The route for the webhook for the messenger bot

    GET request is only for the initial challenge setup by Facebook
    All other requests will be POST
    :return:
    """

    if request.method == 'GET':  # This is for proving ownership of the domain
        supplied_verify = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        logger.debug(f'Challenge: {challenge}')

        if VERIFY != supplied_verify:
            return {"status": "error", "message": "Invalid verification code"}, 403
        return challenge, 200


@app.route('/auth', methods=['POST'])
def auth():
    pass
