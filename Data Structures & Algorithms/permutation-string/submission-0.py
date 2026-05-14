class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            # getting ascii value of each lowercase character
            # it ranges from 0 to 25 since 'a' is 0 and 'z' is 25
            ascii_s1 = ord(s1[i]) - ord('a')
            ascii_s2 = ord(s2[i]) - ord('a')
            s1Count[ascii_s1] += 1
            s2Count[ascii_s2] += 1
        
        for i in range(len(s2) - len(s1)):
            if s1Count == s2Count:
                return True

            index_1 = ord(s2[i]) - ord('a')
            index_2 = ord(s2[i + len(s1)]) - ord('a')
            s2Count[index_1] -= 1
            s2Count[index_2] += 1

        return s1Count == s2Count 