#!/usr/bin/env python
#coding:utf-8

from flask import make_response, jsonify, current_app
from flask import Blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/', methods=["GET"])
def index():
    current_app.logger.info('open page admin')
    resp = make_response(jsonify({'ret': 0}))
    resp.set_cookie('test', '123')
    resp.headers['content-type'] = 'application/json'
    return resp

@admin.app_errorhandler(404)
def page_not_found(e):
    return '<h1 style="text-align:center;color:red;">404  page not found</h1>', 404