#!/usr/bin/env python
#coding:utf-8

from flask import Blueprint, render_template
from datetime import  datetime
blog = Blueprint('blog', __name__)

@blog.route('/', methods=['GET'])
def index():
    args = {'blog_list': [
        {'url': '#', 'title': u'测试', 'img_url': '', 'content': u'论编程语言的鄙视链', 'time_create': datetime.now()},
    ]}
    return render_template('blog/index.html', **args)

@blog.route('/about', methods=['GET'])
def about():
    return render_template('blog/about.html')

@blog.route('/shuo', methods=['GET'])
def shuo():
    return

@blog.route('/diary', methods=['GET'])
def diary():
    return

@blog.route('/photo', methods=['GET'])
def photo():
    return render_template('blog/photo.html')

@blog.route('/learn', methods=['GET'])
def learn():
    return

@blog.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    return

@blog.route('/<int:id>.html')
def info(id):
    return str(id)