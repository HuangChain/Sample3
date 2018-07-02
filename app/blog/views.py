# coding:utf-8
from flask import render_template, request, url_for, redirect, json, jsonify

from . import blog
from ..models import UserInfo, Blog
from .forms import ArticleForm
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


@blog.route('/detail/<int:id>')
def detail(id):
    article = Blog.query.get_or_404(id)
    return render_template('detail.html', article=article)


@blog.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    article = Blog.query.get_or_404(id)
    form = ArticleForm()
    if form.validate_on_submit():
        article.body = form.body.data
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('.articles', id=article.id))
    form.title.data = article.title
    form.body.data = article.body
    return render_template('edit.html', article_form=form)


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


def article_like():
    if request.method == 'POST':
    article_form = ArticleForm()
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        article = Blog(title=data['title'],
                       body=data['body'])
        db.session.add(article)
        db.session.commit()
        return jsonify({'result': 'ok'})
    return render_template('publish.html', article_form=article_form)