#!/usr/bin/env python
#coding:utf-8

import logging
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'passwordd'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    LOGGING_LEVEL = logging.DEBUG

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/flask_dev"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:root@localhost:3306/flask_dev"

class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/flask_db"

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/flask_db"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}