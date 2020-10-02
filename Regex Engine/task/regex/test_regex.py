import unittest
import regex


class TestRegex(unittest.TestCase):
    def test_compare(self):
        self.assertTrue(regex.compare('a', 'a'))
        self.assertTrue(regex.compare('.', 'a'))
        self.assertTrue(regex.compare('', 'a'))
        self.assertTrue(regex.compare('', ''))
        self.assertFalse(regex.compare('a', ''))


if __name__ == "__main__":
    unittest.main()
