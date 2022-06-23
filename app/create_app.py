from flask import Flask


def create_app():
    import config

    flask_app = Flask(__name__)
    flask_app.config["SECRET_KEY"] = config.secret_key

    return flask_app
