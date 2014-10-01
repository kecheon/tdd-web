__author__ = 'cheon'

from flask import make_response
from flask.ext.login import login_required
from . import bid

@bid.route('/')
# @login_required
def index():
    return "<html>InnoMVA</html>"