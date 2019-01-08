#!/usr/bin/env python
#coding:utf-8

from . import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)

    def __repr__(self):
        return '<User %s>' % self.name