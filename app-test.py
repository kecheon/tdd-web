#-*-coding:utf8-*-
from app import app
from flask import Flask, template_rendered, url_for
import unittest
from flask.ext.testing import TestCase

class BasicTestCase(TestCase):
    def create_app(self):
        test_app = app
        app.config['TESTING'] = True
        return test_app

    # user가 홈페이지에 접속한다.
    def test_landing_page(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u"InnoMVA: 주식회사 이노지투비", response.data)

    # user가 우리 사이트를 허섭스러기로 생각한다.
    # 제일 어렵지만 디자인을 입히자.
    def test_use_template(self):
        response = self.client.get('/')
        self.assert_template_used('home.html')

    def test_apply_css(self):
        response = self.client.get(url_for('static', filename='custom.css'))
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()