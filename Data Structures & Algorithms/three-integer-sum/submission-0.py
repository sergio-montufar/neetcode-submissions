class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        answer.add(tuple(temp))
        

        return [list(i) for i in answer]