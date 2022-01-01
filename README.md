## Knapsack Algorithm

knapsack_algorithm is a Python package offering a streamlined and effective resolution for the 0/1 knapsack problem.
### Features

- **Dynamic Programming Solution**: Utilizes dynamic programming to solve the 0/1 knapsack problem efficiently.
- **Error Handling**: Provides comprehensive error handling for input validation.
- **Easy to Use**: Offers a user-friendly interface for solving knapsack problems with given values, weights, and capacity.

### Installation:

You can install KnapsackAlgorithm using pip:

pip install knapsack_algorithm

#### Usage:

Here's an example of how you can use knapsack_algorithm:

from knapsack_algorithm import knapsack

#### Documentation
For detailed documentation and additional options, refer to the official documentation.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

#### Contributing
If you would like to contribute or report issues, please check our contribution guidelines.
#### Example usage:

```bash
values = [60, 100, 120]  # The values of the items

weights = [10, 20, 30]  # The weights of the items

capacity = 50  # The maximum capacity

result = knapsack(values, weights, capacity)

if result is not None:

      print("Maximum value in the knapsack:", result)


