import unittest
from moola_cloud_integration import app

class MoolaCloudIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_routes(self):
        response = self.app.get('/list_routes')
        self.assertEqual(response.status_code, 200)
        self.assertIn('list_routes', str(response.data))

    # Add more tests for other endpoints as needed

if __name__ == '__main__':
    unittest.main()
