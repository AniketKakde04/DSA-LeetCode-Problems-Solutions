class Solution(object):
    # Define a method `removeDuplicates` to remove duplicates from a sorted list `nums`
    def removeDuplicates(self, nums):
        # If the list is empty, return 0
        if not nums:
            return 0
        
        # Initialize a counter to keep track of the position of the unique elements
        count = 1
        
        # Iterate over the list starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous element,
            # it means we have found a unique element
            if nums[i] != nums[i - 1]:
                # Place the unique element at the current count position
                nums[count] = nums[i]
                # Increment the counter
                count += 1
        
        # Return the number of unique elements
        return count

# Define a sorted list of numbers with duplicates
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Create an instance of the Solution class
s = Solution()

# Call the `removeDuplicates` method with the list `nums` and print the result
print(s.removeDuplicates(nums))
