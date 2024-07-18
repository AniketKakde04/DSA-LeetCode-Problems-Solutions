class Solution(object):
    # Define a method `sortColors` to sort the list `nums` containing 0s, 1s, and 2s using Dutch National Flag algorithm
    def sortColors(self, nums):
        # Initialize pointers
        low, mid, high = 0, 0, len(nums) - 1
        
        # Traverse the list
        while mid <= high:
            if nums[mid] == 0:
                # Swap if the current element is 0
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move to the next element if the current element is 1
                mid += 1
            else:
                # Swap if the current element is 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Define a list containing 0s, 1s, and 2s
nums = [2, 0, 2, 1, 1, 0]

# Create an instance of the Solution class
s = Solution()

# Call the `sortColors` method with the list `nums`
s.sortColors(nums)

# Print the sorted list
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
