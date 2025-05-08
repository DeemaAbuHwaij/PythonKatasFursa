import unittest
from katas.stock_trader_v2 import max_profit


class TestMaxProfitMultipleTransactions(unittest.TestCase):

    def test_example_case(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 7)  # Buy at 1 sell at 5, buy at 3 sell at 6

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)  # Buy at 1 sell at 5

    def test_decreasing_prices(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)  # No profit

    def test_alternating_up_down(self):
        prices = [1, 2, 1, 2, 1, 2]
        self.assertEqual(max_profit(prices), 3)  # Buy-sell 3 times

    def test_flat_prices(self):
        prices = [3, 3, 3, 3]
        self.assertEqual(max_profit(prices), 0)

    def test_empty_list(self):
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test_single_price(self):
        prices = [5]
        self.assertEqual(max_profit(prices), 0)

    def test_complex_pattern(self):
        prices = [2, 1, 2, 0, 1]
        self.assertEqual(max_profit(prices), 2)  # Buy at 1 sell at 2, buy at 0 sell at 1

if __name__ == '__main__':
    unittest.main()
