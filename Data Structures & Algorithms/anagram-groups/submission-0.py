from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagram_map = defaultdict(list)


        for string in strs:
            sorted_string = tuple(sorted(string))
            anagram_map[sorted_string].append(string)

        for value in anagram_map.values():
            answer.append(value)

        return answer