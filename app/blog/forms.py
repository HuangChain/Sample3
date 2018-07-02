# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired(message='密码不能为空')])
    body = TextAreaField(u"内容", validators=[DataRequired()])
    submit = SubmitField(u'Submit')