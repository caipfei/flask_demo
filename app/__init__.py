#!/usr/bin/env python
#coding:utf-8

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from .api.views import api
from .admin.views import admin
from .blog.views import blog
db = SQLAlchemy()

def setupLogging(level):
    logging.basicConfig(level=level)
    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024*1024*100, backupCount=10)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    setupLogging(config[config_name].LOGGING_LEVEL)
    db.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(admin)
    app.register_blueprint(blog)

    return app
