#-*-coding:utf8-*-
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # 여기서 한가지 문제점이 발견된다.
    # app.route decorator를 이용해서 정의했던 url을 어찌 처리해야 하나.ㄲ?
    # 이 create_app 펑션은 runtime에서 호출되어 앱을 생성할 텐데 앱이 완전히
    # 생성된 이후라야 app.decorator가 실존할 수 있으니까...
    # blueprint로 해결하다.
    # app/__init__.py 에다가 blueprint를 생성해 놓고
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
