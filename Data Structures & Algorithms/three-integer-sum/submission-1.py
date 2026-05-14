class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answer = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_of_three = a + nums[left] + nums[right]
                if sum_of_three < 0:
                    left += 1
                elif sum_of_three > 0:
                    right -= 1
                else:
                    answer.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return answer   














        # answer = set()
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 answer.add(tuple(temp))
        

        # return [list(i) for i in answer]