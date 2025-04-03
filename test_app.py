import unittest
from app import app
import re

class TestApp(unittest.TestCase):

    def test_hello(self):
        with app.test_client() as client:
            response = client.get('/')
            data = response.data.decode('utf-8')
            self.assertTrue(data.startswith("Hello, World! The current time is "))
            time_str = data[len("Hello, World! The current time is "):]
            self.assertTrue(re.match(r"\d{2}:\d{2}:\d{2}", time_str) is not None)

if __name__ == '__main__':
    unittest.main()
