class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums)-1
        while left < right:
            minimum = left + (right - left) // 2
            if nums[minimum] < nums[right]:
                right = minimum
            else:
                left = minimum + 1
      
        return nums[left]
            
            
        