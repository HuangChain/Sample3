# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired()])
    body = TextAreaField("内容", validators=[DataRequired()])
    submit = SubmitField('Submit')