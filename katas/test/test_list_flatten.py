import unittest
from katas.list_flatten import flatten_list



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(flatten_list([1,[2, 3],[4, [5, 6]],7]), [1, 2, 3, 4, 5, 6, 7])  # add assertion here
    def test2(self):
        self.assertEqual(flatten_list([[1,2, 3],[4, [5, [6]],7]]), [1, 2, 3, 4, 5, 6, 7])  # add assertion here
    def tset3(self):
        self.assertEqual(flatten_list([1,[2, [3],[4, 5, [6]],7]]), [1, 2, 3, 4, 5, 6, 7])  # add assertion here



if __name__ == '__main__':
    unittest.main()


