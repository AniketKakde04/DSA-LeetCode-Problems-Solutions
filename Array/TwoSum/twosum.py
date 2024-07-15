class Solution(object):
    # Define a method `twoSum` that takes a list of numbers (`nums`) and a target value (`target`)
    def twoSum(self, nums, target):
        # Iterate through each element in the list `nums` using index `i`
        for i in range(len(nums)):
            # For each element `i`, iterate through each element again using index `j`
            for j in range(len(nums)):
                # Check if the indices are not the same and if the sum of the elements at these indices equals the target
                if (i != j) and (nums[i] + nums[j] == target):
                    # If the condition is met, return the indices as a list
                    return [i, j]
        
        # If no such pair is found, return an empty list
        return []

# Define a list of numbers and a target value
nums = [2, 7, 11, 15]
target = 9

# Create an instance of the Solution class
s = Solution()

# Call the `twoSum` method with `nums` and `target` and print the result
print(s.twoSum(nums, target))
