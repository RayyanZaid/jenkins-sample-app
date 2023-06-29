import unittest
from maxProbability import maxProbability

class TestMaxProbability(unittest.TestCase):
    def test_example1(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        succProb = [0.5,0.5,0.2]
        start = 0
        end = 2
        expected = 0.25000
        result = maxProbability(n, edges, succProb, start, end)
        self.assertAlmostEqual(result, expected, places=5)

    


if __name__ == '__main__':
    unittest.main()
