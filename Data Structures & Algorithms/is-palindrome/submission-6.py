class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()

        ptr1, ptr2 = 0, len(new_s)-1
        while ptr1 < ptr2:
            while ptr1 < ptr2 and not new_s[ptr1].isalnum():
                ptr1 += 1
            
            while ptr1 < ptr2 and not new_s[ptr2].isalnum():
                ptr2 -= 1
            
            if new_s[ptr1] != new_s[ptr2]:
                return False
            
            ptr1 += 1
            ptr2 -= 1

        return True