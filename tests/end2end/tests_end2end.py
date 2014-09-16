#-*-coding:utf8-*-
__author__ = 'cheon'
from tests_selenium_base import SeleniumTestCase
from flask import request, render_template, url_for
import re
from unittest import skip

# @skip
class WebpageTestCase(SeleniumTestCase):
    def test_home_page(self):
        self.client.get('http://localhost:5000')
        self.assertTrue(re.search('InnoMVA', self.client.page_source))

    def test_login_view(self):
        self.client.get('http://localhost:5000')

        # 유저가 아이디와 비번 입력창을 보다.
        userid_place = self.client.find_element_by_name('userid')
        password_place = self.client.find_element_by_name('password')
        self.assertTrue(userid_place != None)
        self.assertTrue(password_place != None)

        # 유저가 입력창에 아이디/비번을 입력하고 submit 버튼을 클릭한다.
        self.client.find_element_by_name('userid').send_keys('cheon')
        self.client.find_element_by_name('password').send_keys('password')
        self.client.find_element_by_name('submit').click()
        # import pdb; pdb.set_trace()
        # import time
        # time.sleep(10)

        error = None
        try:
            error = self.client.find_element_by_css_selector('.has-error')
            self.assertIn(u'없는 아이디입니다!', error.text)
        except:
            # self.assertFalse(error == None, 'no element which has .has-error')
            self.fail('no element which has .has-error')