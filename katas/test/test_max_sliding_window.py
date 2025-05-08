import unittest
from katas.sliding_window_maximum import max_sliding_window


class TestMaxSlidingWindow(unittest.TestCase):

    def test_example_case(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_two_window(self):
        nums = [9, 11, 3, 4, 8, 7]
        k = 2
        expected = [11, 11, 4, 8, 8]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_single_window(self):
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_entire_window(self):
        nums = [4, 2, 12, 11, -5]
        k = 5
        expected = [12]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_k_equals_len(self):
        nums = [1, 2, 3]
        k = 3
        expected = [3]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_k_zero(self):
        nums = [1, 2, 3]
        k = 0
        expected = []
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_empty_list(self):
        nums = []
        k = 3
        expected = []
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_all_same(self):
        nums = [5, 5, 5, 5, 5]
        k = 3
        expected = [5, 5, 5]
        self.assertEqual(max_sliding_window(nums, k), expected)

if __name__ == '__main__':
    unittest.main()