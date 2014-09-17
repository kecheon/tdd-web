#-*-coding:utf8-*-
__author__ = 'cheon'

from tests_base import BaseTestCase
from app.models import User
from app import db
from unittest import skip

class ViewsTestCase(BaseTestCase):
    def test_login_error_send_back(self):
        response = self.client.post('/', data={'userid':'cheon', 'password':'password'})
        # import pdb; pdb.set_trace()
        # p dir(response)하면 속성을 다 리스팅할 수 있다.
        expected_error = u'없는 아이디입니다!'
        self.assertIn(expected_error, response.data)

    def test_post_and_retrieve(self):

        u = User(password='password', userid='cheon')
        db.session.add(u)

        response = self.client.post('/', data={'userid':'cheon', 'password':'password'})
        retreive = User.query.filter_by(userid = 'cheon').first_or_404()
        self.assertEqual(retreive.userid, 'cheon')