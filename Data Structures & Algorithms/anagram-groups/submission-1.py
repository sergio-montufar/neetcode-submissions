class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # can use lists as keys now
        for s in strs:
            count = [0] * 26
            for c in s:
                # ord() grabs the ASCII value of letter
                # ord('a') is the first letter
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())
