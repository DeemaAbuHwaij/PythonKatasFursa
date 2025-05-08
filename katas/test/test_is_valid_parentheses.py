import unittest
from katas.is_valid_parentheses import is_valid_parentheses

# Assume is_valid_parentheses is defined above or imported

class TestValidParentheses(unittest.TestCase):

    def test_valid_simple(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_valid_nested(self):
        self.assertTrue(is_valid_parentheses("{[]()}"))

    def test_invalid_mismatch(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_invalid_wrong_order(self):
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_only_opening(self):
        self.assertFalse(is_valid_parentheses("((("))

    def test_only_closing(self):
        self.assertFalse(is_valid_parentheses("}}}"))

    def test_single_pair(self):
        self.assertTrue(is_valid_parentheses("()"))

    def test_long_valid(self):
        self.assertTrue(is_valid_parentheses("([]){}[(){}]"))

    def test_long_invalid(self):
        self.assertFalse(is_valid_parentheses("((()))]"))

if __name__ == '__main__':
    unittest.main()
