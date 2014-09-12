from flask import Blueprint, render_template
from app import create_app
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')
