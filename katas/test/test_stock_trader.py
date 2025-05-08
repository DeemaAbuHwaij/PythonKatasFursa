import unittest
from katas.stock_trader import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_example_case(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

    def test_no_profit_possible(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test_single_price(self):
        prices = [5]
        self.assertEqual(max_profit(prices), 0)

    def test_empty_list(self):
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test_profit_at_end(self):
        prices = [9, 2, 6, 1, 7]
        self.assertEqual(max_profit(prices), 6)

    def test_profit_immediate_sell(self):
        prices = [2, 4, 1]
        self.assertEqual(max_profit(prices), 2)

    def test_multiple_valleys_and_peaks(self):
        prices = [3, 2, 6, 1, 5, 4, 8]
        self.assertEqual(max_profit(prices), 7)

if __name__ == '__main__':
    unittest.main()