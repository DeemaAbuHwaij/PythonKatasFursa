import unittest
from katas.stock_trader_v2 import max_profit


class TestMaxProfitMultipleTransactions(unittest.TestCase):

    def test1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 7)

    def test2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)  #

    def test3(self):
        prices = [1, 2, 1, 2, 1, 2]
        self.assertEqual(max_profit(prices), 3)  #

    def test4(self):
        prices = [3, 3, 3, 3]
        self.assertEqual(max_profit(prices), 0)


if __name__ == '__main__':
    unittest.main()
