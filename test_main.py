# Python code
import unittest

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("GitHub Copilot"), "Hello, from GithubAction GitHub Copilot")

if __name__ == '__main__':
    unittest.main()