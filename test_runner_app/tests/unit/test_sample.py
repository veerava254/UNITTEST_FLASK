from app import app
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        result = self.app.get("/")
        self.assertEqual(result.status, '200 OK')
