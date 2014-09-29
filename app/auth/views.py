# -*-coding:utf8-*-
__author__ = 'cheon'

from flask import render_template, session, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from ..models import User
from forms import LoginForm, RegistrationForm
from app import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user =None
    # validate 성공하면 정상적으로 rendering
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
        # import pdb; pdb.set_trace()
            return redirect(url_for('main.index'))
    flash(u'없는 아이디입니다!')
    return render_template('auth/login.html', form=form, user=user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    userid=form.userid.data,
                    password=form.password.data)
        db.session.add(user)
        flash(u'로그인하시면 됩니다!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
