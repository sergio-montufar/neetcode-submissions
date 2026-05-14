class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            print(hashmap)
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
          
            hashmap[nums[i]] = i
        
