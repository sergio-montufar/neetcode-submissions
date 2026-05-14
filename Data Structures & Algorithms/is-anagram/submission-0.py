class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq1 = {}
        freq2 = {}

        for c in s:
            if c in freq1:
                freq1[c] += 1
            else:
                freq1.update({c : 0})

        for c in t:
            if c in freq2:
                freq2[c] += 1
            else:
                freq2.update({c : 0})

        return freq1 == freq2

        