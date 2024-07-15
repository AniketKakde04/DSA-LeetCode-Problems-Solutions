class Solution(object):
    # Define a method `maxArea` to calculate the maximum area of water that can be contained
    def maxArea(self, height):
        # Initialize a variable to keep track of the maximum area found
        maxA = 0
        # Initialize two pointers: `left` at the start and `right` at the end of the list
        left = 0
        right = len(height) - 1

        # Continue the process until the two pointers meet
        while left < right:
            # Calculate the area between the two lines at `left` and `right`
            # Update `maxA` if the calculated area is larger than the current maximum area
            maxA = max(maxA, (right - left) * min(height[left], height[right]))

            # Move the pointer that points to the shorter line inward
            # This is because moving the pointer pointing to the taller line cannot increase the area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the maximum area found
        return maxA

# Define a list of heights representing vertical lines
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Create an instance of the Solution class
s = Solution()

# Call the `maxArea` method with the list `height` and print the result
print(s.maxArea(height))
