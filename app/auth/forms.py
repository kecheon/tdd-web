#-*-coding:utf8-*-
# __author__ = 'cheon'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    userid = StringField(u'아이디', validators=[Required()])
    password = StringField(u'비밀번호', validators=[Required()])
    submit = SubmitField('Submit')