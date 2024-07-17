class Solution(object):
    def plusOne(self, digits):
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 (carry over)
            digits[i] = 0
        
        # If all digits were 9, we need to add a new leading 1
        return [1] + digits

# Define a list of digits representing a number
digits = [1, 2, 3]

# Create an instance of the Solution class
s = Solution()

# Call the `plusOne` method with the list `digits` and print the result
print(s.plusOne(digits))  # Output: [1, 2, 4]

# Test case with all digits being 9
digits = [9, 9, 9]
print(s.plusOne(digits))  # Output: [1, 0, 0, 0]
