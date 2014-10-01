__author__ = 'cheon'
# blueprint of user authentication

from flask import Blueprint

bid = Blueprint('bid', __name__)

from . import views
