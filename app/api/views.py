#!/usr/bin/env python
#coding:utf-8

from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/', methods=["GET", "POST"])
def index():
    return 'hello world'

# @api.app_errorhandler(404)
# def page_not_founc(e):
#     return '<h1 style="text-align:center;">404</h1><h1 style="text-align:center;">page not found</h1>', 404
#
