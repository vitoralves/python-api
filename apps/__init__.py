# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from .api import configure_api
from .jwt import configure_jwt
from .db import db


def create_app(config_name):
    app = Flask('api-users')

    app.config.from_object(config[config_name])

    # Configure MongoEngine
    db.init_app(app)

    configure_jwt(app)
    configure_api(app)

    return app
