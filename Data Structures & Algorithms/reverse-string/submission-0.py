class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s)-1

        for i in range(int(len(s)/2)):
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        