import unittest
from katas.semantic_version_comparator import compare_versions


class TestCompareVersions(unittest.TestCase):

    def test1(self):
        self.assertEqual(compare_versions('1.0.0', '1.0.1'), -1)

    def test2(self):
        self.assertEqual(compare_versions('2.1.0', '1.9.9'), 1)

    def test3(self):
        self.assertEqual(compare_versions('1.2.3', '1.2.3'), 0)

    def test4(self):
        self.assertEqual(compare_versions('1.2', '1.2.0'), 0)

    def test5(self):
        self.assertEqual(compare_versions('1.10.0', '1.2.0'), 1)

    def test6(self):
        self.assertEqual(compare_versions('1.2', '1.2.1'), -1)

    def test7(self):
        self.assertEqual(compare_versions('0.0.0', '0.0.0'), 0)

if __name__ == '__main__':
    unittest.main()