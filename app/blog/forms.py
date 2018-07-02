# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired(message='密码不能为空')])
    body = TextAreaField(u"内容", validators=[DataRequired()])
    submit = SubmitField(u'Submit')


class MesasgeForm(FlaskForm):
    message = TextAreaField(u'留言', validators=[DataRequired(message='不能为空')])
    submit = SubmitField(u'Submit')