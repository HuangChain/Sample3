# coding:utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from .. import db
from .forms import LoginForm
from ..models import UserInfo


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = UserInfo.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):  # 用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
                next = url_for('blog.home')
            return redirect(next)
    return render_template('login.html', login_form=login_form)
