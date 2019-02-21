from flask import Flask
from app.v1.views import office, party


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(office, url_prefix="/api/v1")
    app.register_blueprint(party, url_prefix="/api/v1")
    return  app