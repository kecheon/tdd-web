#-*-coding:utf8-*-
# __author__ = 'cheon'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField(u'Email 주소', validators=[Required()])
    password = StringField(u'비밀번호', validators=[Required()])
    remember_me = BooleanField(u'ID저장')
    submit = SubmitField('확인')


class RegistrationForm(Form):
    email = StringField(u'Email 주소', validators=[Required(), Length(1, 64), Email()])
    userid = StringField('User ID', validators=[ Required(), Length(1, 64),
                  Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                         'Userid must have only letters, '
                         'numbers, dots or underscores')])
    password = PasswordField(u'비밀번호', validators=[ Required(),
                                                      EqualTo('password2',
                                                      message='Passwords must match.')])
    password2 = PasswordField(u'비밀번호 재확인', validators=[Required()])
    submit = SubmitField(u'확인')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'이미 등록된 Email')

    def validate_username(self, field):
        if User.query.filter_by(userid=field.data).first():
            raise ValidationError(u'이미 사용중인 User ID')
