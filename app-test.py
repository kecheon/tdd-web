#-*-coding:utf8-*-
from app import app
import unittest


class BasicTestCase(unittest.TestCase):
    # user가 홈페이지에 접속한다.
    def test_landing_page(self):
        web_client = app.test_client()
        response = web_client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, u"InnoMVA: 주식회사 이노지투비")

if __name__ == "__main__":
    unittest.main()