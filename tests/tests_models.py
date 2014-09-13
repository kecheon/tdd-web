from tests_base import BaseTestCase
from app.models import User
from app import db

class ModelsTestCase(BaseTestCase):

    def test_save_and_retrieve_user(self):
        user1 = User()
        user1.userid = 'myid'
        db.session.add(user1)

        user2 = User()
        user2.userid = 'urid'
        db.session.add(user2)

        users = User.query.all()

        # import pdb; pdb.set_trace()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].userid, 'myid')
        self.assertEqual(users[1].userid, 'urid')
