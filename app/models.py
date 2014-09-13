#-*-coding:utf8-*-
__author__ = 'cheon'

from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError('보지마셈!')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.userid