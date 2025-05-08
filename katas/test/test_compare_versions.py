import unittest
from katas.semantic_version_comparator import compare_versions



class TestCompareVersions(unittest.TestCase):

    def test_less_than(self):
        self.assertEqual(compare_versions('1.0.0', '1.0.1'), -1)

    def test_greater_than(self):
        self.assertEqual(compare_versions('2.1.0', '1.9.9'), 1)

    def test_equal(self):
        self.assertEqual(compare_versions('1.2.3', '1.2.3'), 0)

    def test_missing_patch(self):
        self.assertEqual(compare_versions('1.2', '1.2.0'), 0)

    def test_leading_zeroes_equivalent(self):
        self.assertEqual(compare_versions('01.02.03', '1.2.3'), 0)

    def test_longer_first(self):
        self.assertEqual(compare_versions('1.2.3.4', '1.2.3'), 1)

    def test_longer_second(self):
        self.assertEqual(compare_versions('1.2', '1.2.0.0.1'), -1)

    def test_numeric_comparison(self):
        self.assertEqual(compare_versions('1.10.0', '1.2.0'), 1)
        self.assertEqual(compare_versions('2.0.0', '10.0.0'), -1)

if __name__ == '__main__':
    unittest.main()