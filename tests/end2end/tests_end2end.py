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
        email_place = self.client.find_element_by_name('email')
        password_place = self.client.find_element_by_name('password')
        self.assertTrue(email_place != None)
        self.assertTrue(password_place != None)

        # 유저가 입력창에 아이디/비번을 입력하고 submit 버튼을 클릭한다.
        self.client.find_element_by_name('email').send_keys('somebody@somewhere.com')
        self.client.find_element_by_name('password').send_keys('password')
        self.client.find_element_by_name('submit').click()
        # import pdb; pdb.set_trace()

        # id와 password을 입력하고 서밋하니 그런 아이디 없다고 한다.
        error = None
        try:
            error = self.client.find_element_by_css_selector('.alert')
            self.assertIn(u'없는 아이디입니다!', error.text)
        except:
            self.assertFalse(error == None, 'no element which has .alert')
            self.fail('no element which has .alert')


    #그런 사람 없다 오류가 나서 회원가입을 한다.
    # @skip
    def test_new_user_register(self):
        self.client.get('http://localhost:5000')
        self.assertIsNotNone(self.client.find_element_by_link_text(u'회원가입'))
        self.client.find_element_by_link_text(u'회원가입').click()
        # 회원가입 양식이 나오고 email과 아이디와 비번을 입력하고 전송한다.

        import time

        self.client.find_element_by_name('email').send_keys('somebody@somewhere.com')
        self.client.find_element_by_name('userid').send_keys('somebody')
        self.client.find_element_by_name('password').send_keys('verysecret')
        self.client.find_element_by_name('password2').send_keys('verysecret')
        self.client.find_element_by_name('submit').click()
        time.sleep(3)

        message = self.client.find_element_by_css_selector('.alert')
        self.assertTrue(re.search(u'로그인하시면 됩니다!', message.text))


        # import pdb; pdb.set_trace()
        # self.assertNotEqual(form, [])

        # self.assertFalse(True, 'to make expected Failure')
