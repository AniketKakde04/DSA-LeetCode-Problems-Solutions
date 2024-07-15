class Solution(object):
    # Define a method `findMedianSortedArrays` that takes two sorted lists of numbers (`nums1` and `nums2`)
    def findMedianSortedArrays(self, nums1, nums2):
        # Combine the two lists into one
        nums = nums1 + nums2
        # Sort the combined list
        nums.sort()
        
        # Get the length of the combined list
        x = len(nums)
        
        # Check if the length of the combined list is even
        if x % 2 == 0:
            # Find the two middle elements
            alpha = int(x / 2)
            # Calculate the sum of the two middle elements
            value = nums[alpha - 1] + nums[alpha]
            # Calculate the average of the two middle elements to get the median
            val = (value) / 2
            return val
        # If the length of the combined list is odd
        elif x % 2 != 0:
            # Find the middle element
            alpha = int((x + 1) / 2)
            # The middle element is the median
            val = nums[alpha - 1]
            return val

# Define two sorted lists of numbers
nums1 = [1, 2]
nums2 = [3, 4]

# Create an instance of the Solution class
s = Solution()

# Call the `findMedianSortedArrays` method with `nums1` and `nums2` and print the result
print(s.findMedianSortedArrays(nums1, nums2))
