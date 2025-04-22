import unittest
from katas.is_unique_str import is_unique



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_unique("Hello"), False)
    def test2(self):
        self.assertEqual(is_unique("World"), True)
    def test3(self):
            self.assertEqual(is_unique("Python"), True)
    def test4(self):
        self.assertEqual(is_unique("Unique"), True)

if __name__ == '__main__':
    unittest.main()

