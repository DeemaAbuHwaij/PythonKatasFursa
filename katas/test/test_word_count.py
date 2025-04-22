import unittest
from katas.word_count import count_words


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_words("Hello"), 1)
    def test2(self):
        self.assertEqual(count_words("Hello my"), 2)
    def test3(self):
        self.assertEqual(count_words("Hello my name"), 3)
    def test4(self):
        self.assertEqual(count_words("Hello my name is"), 4)
    def test5(self):
        self.assertEqual(count_words("Hello my name is Deema"), 5)

if __name__ == '__main__':
    unittest.main()
