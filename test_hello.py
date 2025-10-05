import unittest

class TestHello(unittest.TestCase):
    def test_output(self):
        self.assertEqual("Hello from Jenkins Pipeline!", "Hello from Jenkins Pipeline!")

if __name__ == "__main__":
    unittest.main()
