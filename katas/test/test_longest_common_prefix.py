import unittest
from katas.longest_common_prefix import longest_common_prefix


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")  # add assertion here
    def test2(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")  # add assertion here
    def test3(self):
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")  # add assertion here
    def test4(self):
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")  # add assertion here

if __name__ == '__main__':
    unittest.main()

