import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from models import db
from routes.main import main
from routes.api import api
from utils.helpers import add_header
from config.config import Config
from utils.log_filter import RequestFilter

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main)
app.register_blueprint(api)

@app.after_request
def after_request(response):
    return add_header(response)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')

    info_file_handler = RotatingFileHandler('logs/app.log', maxBytes=10 * 1024 * 1024, backupCount=1)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d] [IP: %(client_ip)s]'
    ))
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.addFilter(RequestFilter())
    app.logger.addHandler(info_file_handler)
    error_file_handler = RotatingFileHandler('logs/error.log', maxBytes=10 * 1024 * 1024, backupCount=1)
    error_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d] [IP: %(client_ip)s]'
    ))
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.addFilter(RequestFilter())
    app.logger.addHandler(error_file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('App startup')

if __name__ == '__main__':
    app.run(debug=True)
