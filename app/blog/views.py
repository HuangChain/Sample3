# coding:utf-8
from flask import render_template

from . import blog
from ..models import UserInfo, Blog


@blog.route('/')
def home():
    blogs = Blog.query.all()[:3]
    userinfo=UserInfo.query.filter_by(id=1).first_or_404()
    return render_template('home.html', userinfo=userinfo, blogs=blogs)


@blog.route('/articles')
def articles():
    articles = Blog.query.all()
    return render_template('articles.html', articles=articles)