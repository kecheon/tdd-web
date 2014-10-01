#-*-coding:utf8-*-
__author__ = 'cheon'

import unittest
from flask.ext.testing import TestCase
import threading
from selenium import webdriver

from app import create_app, db


class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        try:
            cls.client = webdriver.Firefox()
            cls.implicitly_wait(3)
        except:
            pass

        if cls.client:
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            db.create_all()
            # User.generate_fake(10)
            threading.Thread(target=cls.app.run).start()

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.close()

            db.drop_all(bind='innoMVA')
            db.session.remove()

            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('no web browser')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()