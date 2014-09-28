# -*-coding:utf8-*-
__author__ = 'cheon'

from flask import render_template, request, current_app, abort
from . import main
from ..models import User
from app.auth.forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
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
    return render_template('home.html', form=form, user=user, error=error)


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