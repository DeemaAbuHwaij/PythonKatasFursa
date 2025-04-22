import unittest
from katas.reduce_list import reduce_array



def list_to_string(array):
    return ' '.join(str(num) for num in array)

class MyTestCase(unittest.TestCase):
    def test1(self):
        input_list = [10, 15, 7, 20, 25]
        reduce_array(input_list)
        self.assertEqual(list_to_string(input_list), "10 5 -8 13 5")
    def test2(self):
        input_list = [0, 5, 10, 15, 20]
        reduce_array(input_list)
        self.assertEqual(list_to_string(input_list), "0 5 5 5 5")
    def test3(self):
        input_list = [20, 18, 10, -2, -4]
        reduce_array(input_list)
        self.assertEqual(list_to_string(input_list), "20 -2 -8 -12 -2")

if __name__ == '__main__':
    unittest.main()

