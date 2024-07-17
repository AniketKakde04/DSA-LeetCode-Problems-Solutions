class Solution(object):
    # Define a method `searchInsert` to find the index at which the target should be inserted
    def searchInsert(self, nums, target):
        # Check if the target is already in the list
        if target in nums:
            # If the target is in the list, return its index
            return nums.index(target)
        else:
            # If the target is not in the list, append it to the list
            nums.append(target)
            # Sort the list to maintain the order
            nums.sort()
            # Return the index of the target in the sorted list
            return nums.index(target)

# Define a list of numbers
nums = [1, 3, 5, 6]
# Define the target value to be inserted
target = 2

# Create an instance of the Solution class
s = Solution()

# Call the `searchInsert` method with the list `nums` and value `target` and print the result
print(s.searchInsert(nums, target))
