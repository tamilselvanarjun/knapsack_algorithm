def knapsack(values, weights, capacity):
    try:
        # Check for input errors
        if len(values) != len(weights):
            raise ValueError("Length of values and weights must be the same.")
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
       
        n = len(values)  # Number of items
        # Create a 2D DP array to store the maximum value that can be obtained using the first i items and capacity
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Build the DP table in bottom-up manner
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i-1] <= w:
                    # If the current item can fit in the knapsack, choose the maximum between taking the item and not taking it
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else:
                    # If the current item cannot fit, do not take it
                    dp[i][w] = dp[i-1][w]

        # The answer to the problem is in dp[n][capacity], which represents considering all items with the full capacity.
        return dp[n][capacity]

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


