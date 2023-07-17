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

    def test_invalid_input_zero_capacity(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 0
        result = knapsack(values, weights, capacity)
        self.assertEqual(result, 0)  # Knapsack capacity is zero, so result should be zero.

    def test_invalid_input_zero_weight(self):
        values = [60, 100, 120]
        weights = [0, 0, 0]
        capacity = 50
        result = knapsack(values, weights, capacity)
        self.assertEqual(result, 0)  # All items have zero weight, so result should be zero.

    def test_valid_input_duplicate_items(self):
        values = [60, 100, 120, 60]  
        weights = [10, 20, 30, 10]  # Duplicate item weight
        capacity = 50
        result = knapsack(values, weights, capacity)
        self.assertEqual(result, 220)  # Duplicate items should not affect the result

if __name__ == '__main__':
    unittest.main()
