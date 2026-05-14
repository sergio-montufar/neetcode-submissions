class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = s.lower()

        left, right = 0, len(new_string)-1
        while left < right:
            while left < right and not new_string[left].isalnum():
                left += 1
            while left < right and not new_string[right].isalnum():
                right -= 1

            if new_string[left] != new_string[right]:
                return False 
            
            left += 1
            right -= 1
        return True