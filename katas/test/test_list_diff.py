import unittest
from katas.list_diff import find_difference


class MyTestCase(unittest.TestCase):
    def tset1(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)  # add assertion here
    def test2(self):
        self.assertEqual(find_difference([0, 3, 1, 6, 10, -20]), 30)  # add assertion here
    def test3(self):
        self.assertEqual(find_difference([10, 30, 5, 6, 20, 1]), 29)  # add assertion here



if __name__ == '__main__':
    unittest.main()


