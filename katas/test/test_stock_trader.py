import unittest
from katas.stock_trader import max_profit

class TestMaxProfit(unittest.TestCase):

    def test1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

    def test2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test3(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test4(self):
        prices = [5]
        self.assertEqual(max_profit(prices), 0)

    def test5(self):
        prices = [2, 4, 1]
        self.assertEqual(max_profit(prices), 2)


if __name__ == '__main__':
    unittest.main()