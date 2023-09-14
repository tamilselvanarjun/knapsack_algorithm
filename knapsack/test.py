import unittest
from your_module_name import knapsack

class TestKnapsack(unittest.TestCase):
    def test_valid_input(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = knapsack(values, weights, capacity)
        self.assertEqual(result, 220)

    def test_invalid_input_different_lengths(self):
        values = [60, 100, 120]
        weights = [10, 20]
        capacity = 50
        result = knapsack(values, weights, capacity)
        self.assertIsNone(result)

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

    def test_large_input(self):
        values = [i for i in range(1, 1001)]  # values = [1, 2, 3, ..., 1000]
        weights = [i for i in range(1, 1001)]  # weights = [1, 2, 3, ..., 1000]
        capacity = 500
        result = knapsack(values, weights, capacity)
        self.assertEqual(result, 125250)  # Sum of values from 1 to 500

if __name__ == '__main__':
    unittest.main()
