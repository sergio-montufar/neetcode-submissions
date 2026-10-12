class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupes = set(nums) # [1, 2, 3, 3] turns into (1, 2, 3)
        if len(no_dupes) != len(nums):
            return True
        else:
            return False