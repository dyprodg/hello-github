# Python code
import unittest
from main import greet  # Import the greet function from main.py

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("GitHub", "Copilot"), "Hello, from GithubAction GitHub Copilot")

if __name__ == '__main__':
    unittest.main()