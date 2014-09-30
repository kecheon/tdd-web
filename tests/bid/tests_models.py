__author__ = 'cheon'

from tests.tests_base import BaseTestCase
from app.bid.models import Bid
from app import db


class ModelsTestCase(BaseTestCase):

    def test_bid_query(self):
        bids = Bid.query.limit(10)
        self.assertEqual(bids.count(), 10)