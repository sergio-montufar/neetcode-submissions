class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        chosen = [False] * len(nums)
        

        def backtrack(i):
            # print(i)
            if i == len(nums):
                result.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                backtrack(i+1)
                nums[j], nums[i] = nums[i], nums[j]
        

        backtrack(0)
        return result


