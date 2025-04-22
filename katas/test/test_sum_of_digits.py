import unittest
from katas.sum_of_digits import sum_of_digits



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_of_digits("abc123"), 6)
    def test2(self):
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)
    def test3(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)



if __name__ == '__main__':
    unittest.main()

