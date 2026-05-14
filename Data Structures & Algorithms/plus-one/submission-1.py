class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            incremented_digit = digits[i] + 1
            print(incremented_digit)
            if incremented_digit <= 9:
                digits[i] = incremented_digit
                return digits
            elif incremented_digit > 9:
                digits[i] = 0
                
        digits.insert(0, 1)
        return digits