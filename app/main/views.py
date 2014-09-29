# -*-coding:utf8-*-
__author__ = 'cheon'

from flask import render_template, request, current_app, abort, flash
from . import main
from ..models import User
from app.auth.forms import LoginForm
from flask.ext.login import logout_user, login_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('home.html')


@main.route('/shutdown')
def server_shutdown():
    # import pdb; pdb.set_trace()

    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'