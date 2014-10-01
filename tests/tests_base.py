#-*-coding:utf8-*-
from app import create_app, db
from flask import url_for, current_app
import unittest
from flask.ext.testing import TestCase
from unittest import skip


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all(bind='innoMVA') # 공고가 있는 main db(innobid)는 드롭하면 안되고 test db만 드롭
        self.app_context.pop()

    def create_app(self):
        """must for TestCase
        """
        return create_app(self)


class FlaskBaseTestCase(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all(bind='innoMVA') # 공고가 있는 main db(innobid)는 드롭하면 안되고 test db만 드롭
        self.app_context.pop()

    def create_app(self):
        """must for TestCase
        """
        return create_app(self)


class FunctionalTestCase(BaseTestCase):

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    # user가 홈페이지에 접속한다.
    def test_landing_page(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u"InnoMVA: 주식회사 이노지투비", response.data)

    # user가 우리 사이트를 허섭스러기로 생각한다.
    # 제일 어렵지만 디자인을 입히자.
    # assert_template_used는 TestCase의 method인데,
    # unittest에다가 flask-testing TestCase를 integrate 못해서 보류키로 한다.

    # def test_use_template(self):
    #     response = self.client.get('/')
    #     self.assert_template_used('home.html')

    def test_apply_css(self):
        response = self.client.get(url_for('static', filename='custom.css'))
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()