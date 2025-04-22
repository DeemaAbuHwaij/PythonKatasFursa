import unittest
from katas.do_n_times import do_n_times, say_hello, print_message


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(do_n_times(say_hello,3),"")  # add assertion here


if __name__ == '__main__':
    unittest.main()
