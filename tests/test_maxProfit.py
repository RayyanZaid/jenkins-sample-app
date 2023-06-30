import unittest
from maxProfit import maxProfit


class TestMaxProfit(unittest.TestCase):
    def test_leetcodeCase(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5

        result = maxProfit(prices)

        self.assertEqual(result, expected)

    def test_leetcodeCase2(self):
        prices = [7,6,4,3,1]
        expected = 0

        result = maxProfit(prices)

        self.assertEqual(result, expected)

    def test_edgeCase(self):
        prices = [0,0,0,0]
        expected = 0
        result = maxProfit(prices)
        self.assertEqual(result,expected)


if __name__ == "__main__":
    unittest.main()
