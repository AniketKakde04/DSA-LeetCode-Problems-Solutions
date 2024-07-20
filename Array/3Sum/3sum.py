class Solution(object):
    # Define a method `threeSum` to find all unique triplets in the list `nums` that sum to zero
    def threeSum(self, nums):
        # Initialize a set to store unique triplets
        ans = set()
        # Sort the list
        nums.sort()
        # Get the length of the list
        n = len(nums)
        # Iterate through the list with three nested loops (inefficient)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    # Calculate the sum of the triplet
                    temp = nums[i] + nums[j] + nums[k]
                    # If the sum is zero, add the triplet to the set
                    if temp == 0:
                        ans.add((nums[i], nums[j], nums[k]))
        # Return the set of unique triplets
        return ans

# Define a list of numbers
nums = [-1, 0, 1, 2, -1, -4]

# Create an instance of the Solution class
s = Solution()

# Call the `threeSum` method with the list `nums` and print the result
print(s.threeSum(nums))
