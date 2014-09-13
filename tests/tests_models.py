from tests_base import BaseTestCase
from app.models import User
from app import db

class UserModelTestCase(BaseTestCase):

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

    def test_password_setter(self):
        u = User(password = 'hotdog')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_get(self):
        u = User(password = 'hotdog')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='hotdog')
        self.assertTrue(u.verify_password('hotdog'))
        self.assertFalse(u.verify_password('cooldog'))

    def test_password_salts_random(self):
        u1 = User(password='hotdog')
        u2 = User(password='cooldog')
        self.assertTrue(u1.password_hash != u2.password_hash)