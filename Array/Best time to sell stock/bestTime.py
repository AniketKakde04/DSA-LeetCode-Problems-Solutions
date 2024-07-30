class Solution(object):
    # Define a method `maxProfit` to find the maximum profit from buying and selling a stock
    def maxProfit(self, prices):
        # Initialize `buy` with the first price in the list
        buy = prices[0]
        # Initialize `profit` to 0
        profit = 0

        # Iterate through the list of prices starting from the second price
        for i in range(1, len(prices)):
            # If the current price is less than `buy`, update `buy` to the current price
            if prices[i] < buy:
                buy = prices[i]
            # If the profit from selling at the current price is greater than the current `profit`, update `profit`
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        
        # Return the maximum profit
        return profit

# Define a list of stock prices
prices = [7, 1, 5, 3, 6, 4]

# Create an instance of the Solution class
s = Solution()

# Call the `maxProfit` method with the list `prices` and print the result
print(s.maxProfit(prices))  # Output: 5
