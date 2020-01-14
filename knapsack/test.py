import unittest
from knapsack_algorithm import knapsack

class TestKnapsack(unittest.TestCase):
    def test_valid_input(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = knapsack(values, weights, capacity)
        self.assertEqual(result, 220)

    def test_invalid_input_negative_capacity(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = -50
        result = knapsack(values, weights, capacity)
        self.assertIsNone(result)

    def test_invalid_input_empty_lists(self):
        values = []
        weights = []
        capacity = 50
        result = knapsack(values, weights, capacity)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
