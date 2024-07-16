class Solution(object):
    # Define a method `removeElement` to remove all occurrences of `val` from the list `nums`
    def removeElement(self, nums, val):
        # Loop while `val` is in `nums`
        while val in nums:
            # Remove the first occurrence of `val` in `nums`
            nums.remove(val)
        
        # Return the length of the modified list
        return len(nums)

# Define a list of numbers
nums = [3, 2, 2, 3]
# Define the value to be removed
val = 3

# Create an instance of the Solution class
s = Solution()

# Call the `removeElement` method with the list `nums` and value `val` and print the result
print(s.removeElement(nums, val))
print(nums)