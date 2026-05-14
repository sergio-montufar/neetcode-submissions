class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        freq = set(s)

        for c in freq:
          count = left = 0
          for right in range(len(s)):
            if s[right] == c:
                count += 1

            while (right - left + 1) - count > k:
                if s[left] == c:
                    count -= 1
                left += 1
            
            ans = max(right - left + 1, ans)

        return ans





        