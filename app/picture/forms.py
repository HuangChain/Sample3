# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import  SubmitField, ValidationError, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class PictureForm(FlaskForm):
    upload = FileField('image',validators=[FileRequired()])
    submit = SubmitField(u'上传')
