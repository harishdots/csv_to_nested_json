from flask import Flask
from os import path

def create_app():
    app = Flask(__name__)

    from .views import views
    from . import csv_to_json_tree

    app.register_blueprint(views, url_prefix='/')

    return app
