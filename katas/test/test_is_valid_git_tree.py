import unittest
from katas.is_valid_git_tree import is_valid_git_tree
from io import StringIO
from unittest.mock import patch

# Assuming is_valid_git_tree is in the same file or already imported

class TestGitTreeValidation(unittest.TestCase):

    def test_valid_tree(self):
        tree = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_cycle_in_tree(self):
        tree = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]  # cycle here
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_multiple_roots(self):
        tree = {
            "A": ["B"],
            "C": ["D"],
            "B": [],
            "D": []
        }
        self.assertFalse(is_valid_git_tree(tree))  # Two roots: A and C

    def test_disconnected_tree(self):
        tree = {
            "A": ["B"],
            "B": [],
            "C": []  # Disconnected node
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_single_node_tree(self):
        tree = {
            "A": []
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_empty_tree(self):
        tree = {}
        self.assertFalse(is_valid_git_tree(tree))  # No nodes means no root

if __name__ == '__main__':
    unittest.main()
