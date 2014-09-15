#-*-coding:utf8-*-
__author__ = 'cheon'

from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import User
from forms import LoginForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('home.html', form=form)



