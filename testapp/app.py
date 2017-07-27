import logging

from flask import Blueprint, Flask, render_template, redirect, request, url_for
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
page = Blueprint('page', __name__)


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)
    app.logger.addHandler(stream_handler)

    return app


@page.route('/')
def index():
    return "HELLO"
