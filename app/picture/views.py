# coding:utf-8

from flask import request, redirect, url_for, render_template
from . import picture
from .forms import PictureForm
import os


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@picture.route('/pictures', methods=['GET', 'POST'])
def pictures():
    form = PictureForm()
    if request.method == 'POST':
        img = request.files.get('upload')
        path = os.path.join(basedir, 'static/media/')+img.filename
        img.save(path)
        return redirect(url_for('.pictures'))
    a = os.walk(os.path.join(basedir, 'static/media/'))
    b = list(a)[0][2]
    return render_template('pictures.html', form=form, pictures=b)

