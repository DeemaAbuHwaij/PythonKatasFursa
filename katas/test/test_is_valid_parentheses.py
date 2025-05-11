import unittest
from katas.is_valid_parentheses import is_valid_parentheses

# Assume is_valid_parentheses is defined above or imported

class TestValidParentheses(unittest.TestCase):

    def test_valid1(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_valid2(self):
        self.assertTrue(is_valid_parentheses("{[]()}"))

    def test_valid3(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_valid4(self):
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_valid5(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_valid6(self):
        self.assertFalse(is_valid_parentheses("((("))

    def test_valid7(self):
        self.assertFalse(is_valid_parentheses("}}}"))

    def test_valid8(self):
        self.assertTrue(is_valid_parentheses("()"))

if __name__ == '__main__':
    unittest.main()
