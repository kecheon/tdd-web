# -*-coding:utf8-*-
__author__ = 'cheon'

from flask import render_template, session, redirect, url_for
from . import auth
from ..models import User
from forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    userid = None
    password = None
    form = LoginForm()
    user = None
    error = None
    # validate 성공하면 정상적으로 rendering
    if form.validate_on_submit():
        userid = form.userid.data
        password = form.password.data
        # 좀비가 생기면 안되니까
        form.userid.data = ''
        form.password.data = ''
        user = User.query.filter_by(userid=userid).first()
        if not user:
            error = u'없는 아이디입니다!'
        # import pdb; pdb.set_trace()
    return render_template('auth/login.html', form=form, user=user, error=error)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', form=form)
