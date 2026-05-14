class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        max_length = 0
        left, right = 0, 0
        freq = set()

        while right < len(s):
            while s[right] in freq:
                freq.remove(s[left])
                left += 1

            freq.add(s[right])
            curr_max = right - left + 1
            max_length = max(curr_max, max_length)
            # print(f'left: ({left},{s[left]}), right: ({right}, {s[right]})')
            # print("length of max substring:", max_length)
            right += 1
            
        return max_length

