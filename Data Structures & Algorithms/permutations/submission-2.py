class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        chosen = [False] * len(nums)

        def backtrack(iteration):
            if len(iteration) == len(nums):
                result.append(iteration.copy())
                return
            
            for i in range(len(nums)):
                if not chosen[i]:
                    iteration.append(nums[i])
                    chosen[i] = True
                    backtrack(iteration)
                    iteration.pop()
                    chosen[i] = False
        

        backtrack([])
        return result






        # result = []
        
        # def backtrack(i):
        #     # print(i)
        #     if i == len(nums):
        #         result.append(nums[:])
        #         return
        #     for j in range(i, len(nums)):
        #         nums[j], nums[i] = nums[i], nums[j]
        #         backtrack(i+1)
        #         nums[j], nums[i] = nums[i], nums[j]
        

        # backtrack(0)
        # return result


