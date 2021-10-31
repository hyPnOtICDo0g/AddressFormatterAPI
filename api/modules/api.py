import logging
from .parser import v1, v2
from flask import Flask, request
from flask_limiter import Limiter
from werkzeug.exceptions import BadRequest
from flask_limiter.util import get_remote_address

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False
limit_requests = Limiter(
    api,
    key_func=get_remote_address,
    default_limits=["4000/day"]
)

# pipe flask logs through gunicorn
gunicorn_logger = logging.getLogger('gunicorn.error')
api.logger.handlers = gunicorn_logger.handlers
api.logger.setLevel(gunicorn_logger.level)

def json_details(message, status):
    json_data=({"message": message,
                "status": str(status)})
    return json_data, status

# allow only POST requests
@api.route('/', methods = ['POST'])
def home():
    api.logger.info(f"Request IP: {get_remote_address()}; homepage")
    message="API lies at the '/api' endpoint."
    return json_details(message, 200)

@api.route('/api', methods = ['POST'])
def api_home():
    if request.method == 'POST':
        api.logger.info(f"Request IP: {get_remote_address()}; apihome")
        message="Welcome to the Address Formatter API. Please read the docs for it's usage."
        return json_details(message, 200)

@api.route('/api/v1', methods = ['POST'])
@limit_requests.limit("150/minute;4/second")
def api_v1():
    try:
        if request.method == 'POST':
            api.logger.info(f"Request IP: {get_remote_address()}; apiv1")
            return v1(request.get_json(force=True)), 200
    except BadRequest:
        message="POST JSON only."
        return json_details(message, 415)

@api.route('/api/v2', methods = ['POST'])
@limit_requests.limit("150/minute;4/second")
def api_v2():
    try:
        if request.method == 'POST':
            api.logger.info(f"Request IP: {get_remote_address()}; apiv2")
            return v2(request.get_json(force=True)), 200
    except BadRequest:
        message="POST JSON only."
        return json_details(message, 415)

# several error handlers
@api.errorhandler(404)
def error_404(error):
    api.logger.info(f"Request IP: {get_remote_address()}; 404")
    message="Oops! You stumbled upon the wrong page I guess."
    return json_details(message, 404)

@api.errorhandler(405)
def error_405(error):
    api.logger.info(f"Request IP: {get_remote_address()}; 405")
    message="Oops! POST requests only, read the docs."
    return json_details(message, 405)

@api.errorhandler(429)
def error_429(error):
    api.logger.info(f"Request IP: {get_remote_address()}; 429")
    message="Oops! Too Many Requests."
    return json_details(message, 429)

@api.errorhandler(Exception)
def error_unexpected(error):
    api.logger.exception(f"Request IP: {get_remote_address()}; Error: {error}")
    message="Uhh...Something went wrong."
    return json_details(message, 500)

def api_init():
    return api
