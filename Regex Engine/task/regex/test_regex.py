import unittest
import regex


class Test(unittest.TestCase):
    def test_match(self):
        self.assertTrue(regex.check_repetition('colou?r', 'color'))
        self.assertTrue(regex.check_repetition('colou?r', 'colour'))
        self.assertFalse(regex.check_repetition('colou?r', 'colouur'))
        self.assertTrue(regex.check_repetition('colou*r', 'color'))
        self.assertTrue(regex.check_repetition('colou*r', 'colour'))
        self.assertTrue(regex.check_repetition('colou*r', 'colouur'))
        self.assertTrue(regex.check_repetition('col.*r', 'color'))
        self.assertTrue(regex.check_repetition('col.*r', 'colour'))
        self.assertTrue(regex.check_repetition('col.*r', 'colr'))
        self.assertTrue(regex.check_repetition('col.*r', 'collar'))
        self.assertFalse(regex.check_repetition('col.*r$', 'colors'))


if __name__ == '__main__':
    unittest.main()
