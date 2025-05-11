import unittest
from katas.max_storage_capacity import max_storage_area
# Assume max_storage_area is defined above or imported

class TestMaxStorageArea(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_example2(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_example3(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)  # 3 * 3 (index 2 to 4)

    def test_example4(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)  # 3 * 3 (index 0 to 2)

    def test_example5(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)  # 4 * 3

    def test_example6(self):
        self.assertEqual(max_storage_area([2, 1, 2]), 3)

    def test_example7(self):
        self.assertEqual(max_storage_area([]), 0)


if __name__ == '__main__':
    unittest.main()
