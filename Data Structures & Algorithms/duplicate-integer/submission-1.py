class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupes = list(set(nums))
        print(len(noDupes))
        print(len(nums))
        return not (len(noDupes) == len(nums))