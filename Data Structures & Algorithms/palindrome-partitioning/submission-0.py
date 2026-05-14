class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i, j, iteration):
            if i >= len(s):
                if i == j:
                    result.append(iteration.copy())
                return
            # if the substring is equal to it's reverse
            # then it is a palindrome
            
            if s[j:i+1] == s[j:i+1][::-1]:
                iteration.append(s[j:i+1])
                backtrack(i+1, i+1, iteration)
                iteration.pop()
                
                
            backtrack(i+1, j, iteration)

        backtrack(0, 0, [])
        return result