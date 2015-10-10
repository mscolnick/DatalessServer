import logging
from flask import Flask, request as req
from app.controllers.database import db
from app.controllers import pages
from config.development import SQLALCHEMY_DATABASE_URI
import os

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)
    app.register_blueprint(pages.blueprint)

    app.logger.setLevel(logging.NOTSET)

    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    if not os.path.isfile(SQLALCHEMY_DATABASE_URI):
        setup_database(app)
    return app

def setup_database(app):
    with app.app_context():
        db.create_all()
