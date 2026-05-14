class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2": "abc", "3": "def", "4": "ghi",
                   "5": "jkl", "6": "mno", "7": "pqrs", 
                   "8": "tuv", "9": "wxyz"}
        result = []

        def backtrack(i, str_iter):
            if len(str_iter) == len(digits):
                result.append(str_iter)
                return

            letters = hashmap[digits[i]]
            for l in letters:
                backtrack(i+1, str_iter+l)
                
                
            
        if digits:
            backtrack(0, "")
        return result
        