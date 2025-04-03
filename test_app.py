import unittest
import app
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Hello, World!')
        self.assertIn('timestamp', data)
        # You might want to add a more specific check for the timestamp format

if __name__ == '__main__':
    unittest.main()
