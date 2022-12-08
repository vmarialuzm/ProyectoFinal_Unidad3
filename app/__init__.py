from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .routes.api import api_ruta



def create_app(): #fx de fabrica
    app=Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    app.register_blueprint(api_ruta)
    return app