from flask import Blueprint, render_template
from app import create_app
main = Blueprint('main', __name__)

from . import views
