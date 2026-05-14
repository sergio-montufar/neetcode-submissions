class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, iterator):
            if index == len(nums):
                result.append(iterator.copy())
                return

            iterator.append(nums[index])
            backtrack(index+1, iterator)
            
            while index + 1 < len(nums) and nums[index+1] == nums[index]:
                index += 1;
                
            iterator.pop()
            backtrack(index+1, iterator)
            
            

        backtrack(0, [])
        return result
