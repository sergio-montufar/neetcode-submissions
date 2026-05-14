class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_arr = []

        def backtrack(i=0):
            if i == len(nums):
                result.append(curr_arr[:])
                return
            
            backtrack(i+1)

            curr_arr.append(nums[i])
            backtrack(i+1)
            curr_arr.pop()

        backtrack()
        return result

    
        