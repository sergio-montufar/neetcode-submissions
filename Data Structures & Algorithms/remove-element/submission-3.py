class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)-1, -1, -1):
            # print(val, nums[i])
            if val == nums[i]:
                count += 1
                nums.pop(i)

        
        
        return len(nums)