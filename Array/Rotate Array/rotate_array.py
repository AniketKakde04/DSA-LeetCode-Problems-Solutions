class Solution(object):
    def rotate(self, nums, k):
        nums_new = []

        # Add last k elements from nums to nums_new
        for i in range(-k, 0):
            nums_new.append(nums[i])
        
        # Add the rest of the elements to nums_new
        nums_new.extend(nums[:-k])
        
        # Modify nums in place
        for i in range(len(nums)):
            nums[i] = nums_new[i]

s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
