__author__ = 'cheon'
# blueprint of user authentication

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
