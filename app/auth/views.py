# coding:utf-8
from flask import render_template, redirect, request, url_for
from flask_login import login_user, login_required, logout_user
from . import auth
from .. import db
from .forms import LoginForm
from ..models import UserInfo, Message


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            user = UserInfo.query.filter_by(email=login_form.email.data).first()
            if user.password == login_form.data['password']:
                login_user(user)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('blog.home')
                return redirect(next)
    return render_template('login.html', login_form=login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.home'))


@auth.route('/verify/', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        message = Message.query.filter_by(id=request.form['id']).first()
        status = request.form['status']
        message.status=int(status)
        db.session.add(message)
        db.session.commit()
        return "1"


