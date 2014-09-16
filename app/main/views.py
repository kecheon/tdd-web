#-*-coding:utf8-*-
__author__ = 'cheon'

from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import User
from forms import LoginForm

@main.route('/', methods=['GET', 'POST'])
def index():
    userid = None
    password = None
    form = LoginForm()
    u1 = None
    # validate 성공하면 정상적으로 rendering
    if form.validate_on_submit():
        userid = form.userid.data
        password = form.password.data
        # 좀비가 생기면 안되니까
        form.userid.data = ''
        form.password.data = ''
        u1 = User.query.filter_by(userid = userid).first()

    return render_template('home.html', form=form, user=u1)

