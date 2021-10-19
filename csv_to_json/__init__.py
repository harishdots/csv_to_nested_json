from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import views
    from . import csv_to_json_tree

    app.register_blueprint(views, url_prefix='/')

    return app
