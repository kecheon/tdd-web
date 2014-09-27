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

        # id와 password을 입력하고 서밋하니 그런 아이디 없다고 한다.
        error = None
        try:
            error = self.client.find_element_by_css_selector('.has-error')
            self.assertIn(u'없는 아이디입니다!', error.text)
        except:
            self.assertFalse(error == None, 'no element which has .has-error')
            self.fail('no element which has .has-error')
        form1 = None
        form1 = self.client.find_elements_by_css_selector('.has-error')
        print "hello %s" % form1

    #그런 사람 없다 오류가 나서 회원가입을 한다.
    def test_new_user_register(self):
        self.client.get('http://localhost:5000')
        self.assertIsNotNone(self.client.find_element_by_link_text(u'회원가입'))
        self.client.find_element_by_link_text(u'회원가입').click()
        # 회원가입 양식이 나오고 아이디와 비번을 입력하고 전송한다.
        # import time
        # time.sleep(10)

        # import pdb; pdb.set_trace()
        # self.assertNotEqual(form, [])

        # self.assertFalse(True, 'to make expected Failure')
