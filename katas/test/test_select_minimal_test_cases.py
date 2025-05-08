import unittest
from katas.requirements_coverage import select_minimal_test_cases


class TestSelectMinimalTestCases(unittest.TestCase):

    def test_basic_case(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [2, 3])  # Covers 1, 2, 3, 4, 5

    def test_minimal_exact(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0, 1, 2, 3, 4])  # Must take all

    def test_overlapping_minimal(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [3, 4],
            [1, 4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0, 2])  # One possible minimal set

    def test_large_overlap(self):
        test_cases = [
            [1, 2, 3, 4, 5],
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])  # One test case covers everything

    def test_already_minimal(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [3, 1]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(len(result), 2)  # Any 2 of the 3 will do

if __name__ == '__main__':
    unittest.main()