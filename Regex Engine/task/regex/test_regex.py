import unittest
import regex


class Test(unittest.TestCase):
    def test_match(self):
        self.assertTrue(regex.match('^app', 'apple'))
        self.assertTrue(regex.match('^a', 'apple'))
        self.assertTrue(regex.match('^apple', 'apple pie'))
        self.assertFalse(regex.match('^le', 'apple'))
        self.assertTrue(regex.match('le$', 'apple'))
        self.assertTrue(regex.match('.$', 'apple'))
        self.assertTrue(regex.match('apple$', 'tasty apple'))
        self.assertFalse(regex.match('app$', 'apple'))
        self.assertTrue(regex.match('^apple$', 'apple'))
        self.assertFalse(regex.match('^apple$', 'tasty apple'))
        self.assertFalse(regex.match('^apple$', 'apple pie'))
        self.assertFalse(regex.match('^app$', 'apple'))


if __name__ == '__main__':
    unittest.main()
