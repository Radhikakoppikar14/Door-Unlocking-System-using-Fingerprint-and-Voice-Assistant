import unittest
import json
from app import create_app
from models import db

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_projects(self):
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
