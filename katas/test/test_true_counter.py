import unittest
from katas.true_counter import count_true_values



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)
    def test2(self):
        self.assertEqual(count_true_values([True, True, True, True, True]), 5)
    def test3(self):
        self.assertEqual(count_true_values([True, True, False]), 2)
    def test4(self):
        self.assertEqual(count_true_values([False, False, False]), 0)
    def test5(self):
        self.assertEqual(count_true_values([False, False, False, True]), 1)

if __name__ == '__main__':
    unittest.main()



