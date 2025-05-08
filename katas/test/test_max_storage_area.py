import unittest
from katas.max_storage_capacity import max_storage_area
# Assume max_storage_area is defined above or imported

class TestMaxStorageArea(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_single_bar(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_increasing_heights(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)  # 3 * 3 (index 2 to 4)

    def test_decreasing_heights(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)  # 3 * 3 (index 0 to 2)

    def test_all_same_height(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)  # 4 * 3

    def test_alternating_heights(self):
        self.assertEqual(max_storage_area([2, 1, 2]), 3)

    def test_empty(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_zero_height_bars(self):
        self.assertEqual(max_storage_area([0, 0, 0]), 0)

    def test_large_valley(self):
        self.assertEqual(max_storage_area([6, 2, 5, 4, 5, 1, 6]), 12)  # Classic example

if __name__ == '__main__':
    unittest.main()
