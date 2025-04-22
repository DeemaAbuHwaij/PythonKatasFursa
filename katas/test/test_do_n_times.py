import unittest
from katas.do_n_times import do_n_times, say_hello, print_message
from io import StringIO
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test1(self):
        with patch('sys.stdout', new=StringIO()) as sysout:
            do_n_times(say_hello, 3)
            self.assertEqual(sysout.getvalue(), "Hello!\nHello!\nHello!\n")
    def test2(self):
        with patch('sys.stdout', new=StringIO()) as sysout:
            do_n_times(print_message, 5)
            self.assertEqual(sysout.getvalue(), "Python is fun!\nPython is fun!\nPython is fun!\nPython is fun!\nPython is fun!\n")


if __name__ == '__main__':
    unittest.main()
