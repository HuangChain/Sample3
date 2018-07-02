# coding:utf-8
from flask import render_template, request, url_for, redirect, json, jsonify

from . import blog
from ..models import UserInfo, Blog, Message
from .forms import ArticleForm, MesasgeForm
from .. import db


@blog.route('/')
def home():
    blogs = Blog.query.all()[:3]
    userinfo=UserInfo.query.filter_by(id=1).first_or_404()
    return render_template('home.html', userinfo=userinfo, blogs=blogs)


@blog.route('/articles/')
def articles():
    page = request.args.get('page', 1, type=int)
    pagination = Blog.query.order_by(Blog.publish.desc()).paginate(
        page, per_page=3,
        error_out=False)
    posts = pagination.items
    return render_template('articles.html', posts=posts, pagination=pagination)


@blog.route('/detail/<int:id>', methods=['GET', 'POST'])
def detail(id):
    article = Blog.query.get_or_404(id)
    if request.method == 'POST':
        article.likes += 1
        db.session.add(article)
        db.session.commit()
        return jsonify({'result': 'ok'})
    likes = range(article.likes)
    return render_template('detail.html', article=article, likes=likes)


@blog.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    article = Blog.query.get_or_404(id)
    form = ArticleForm()
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        article.title = data['title']
        article.body = data['body']
        db.session.add(article)
        db.session.commit()
        return jsonify({'result': 'ok'})
    form.title.data = article.title
    form.body.data = article.body
    return render_template('edit.html', article_form=form, article=article)


@blog.route('/publish/', methods=['GET', 'POST'])
def publish():
    article_form = ArticleForm()
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        article = Blog(title=data['title'],
                       body=data['body'])
        db.session.add(article)
        db.session.commit()
        return jsonify({'result': 'ok'})
    return render_template('publish.html', article_form=article_form)


@blog.route('/delete_article/<int:id>', methods=['GET', 'POST'])
def delete_article(id):
    if request.method == 'POST':
        Blog.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'result': 'ok'})


@blog.route('/messages/', methods=['GET', 'POST'])
def messages():
    message_form = MesasgeForm()
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        message = Message(message=data['message'])
        db.session.add(message)
        db.session.commit()
        return jsonify({'result': 'ok'})
    page = request.args.get('page', 1, type=int)
    pagination = Message.query.order_by(Message.created.desc()).paginate(
        page, per_page=3,
        error_out=False)
    messages = pagination.items
    return render_template('messages.html', messages=messages, pagination=pagination, message_form=message_form)


