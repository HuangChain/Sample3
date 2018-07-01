# coding:utf-8
from datetime import datetime
from . import db
from flask_login import UserMixin


class UserInfo(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(64), unique=True, index=True)
    birthday = db.Column(db.DateTime, default=datetime.utcnow)
    position = db.Column(db.String(64))
    hobby = db.Column(db.String(64))
    address = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.Text())
    publish = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.title

