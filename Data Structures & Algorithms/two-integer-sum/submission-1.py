class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in sum_dict:
                return [sum_dict[difference], i]
            sum_dict[num] = i