import unittest
from moola_cloud_integration import app

class MoolaCloudIntegrationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_create_spark_valid(self):
        response = self.app.post('/create_spark', json={'name': 'Test Spark'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Spark created successfully!', response.get_data(as_text=True))

    def test_create_spark_invalid(self):
        response = self.app.post('/create_spark', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input, 'name' is required.", response.get_data(as_text=True))

    def test_foundry_integration_valid(self):
        response = self.app.post('/foundry_integration', json={'integration_id': '12345'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Integration with Microsoft Foundry successful!', response.get_data(as_text=True))

    def test_foundry_integration_invalid(self):
        response = self.app.post('/foundry_integration', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input, data is required.", response.get_data(as_text=True))

    def test_foundry_data_valid(self):
        response = self.app.post('/foundry_data', json={'data': 'Sample Data'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Data managed successfully with Microsoft Foundry!', response.get_data(as_text=True))

    def test_foundry_data_invalid(self):
        response = self.app.post('/foundry_data', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input, 'data' is required.", response.get_data(as_text=True))

    def test_rubin_integration_valid(self):
        response = self.app.post('/rubin_integration', json={'rubin_id': 'RUBIN123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Integration with NVIDIA RUBIN successful!', response.get_data(as_text=True))

    def test_rubin_integration_invalid(self):
        response = self.app.post('/rubin_integration', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input, 'rubin_id' is required.", response.get_data(as_text=True))

    def test_blackwell_ultra_integration_valid(self):
        response = self.app.post('/blackwell_ultra_integration', json={'blackwell_id': 'BLACKWELL123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Integration with NVIDIA BLACKWELL ULTRA successful!', response.get_data(as_text=True))

    def test_blackwell_ultra_integration_invalid(self):
        response = self.app.post('/blackwell_ultra_integration', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input, 'blackwell_id' is required.", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
