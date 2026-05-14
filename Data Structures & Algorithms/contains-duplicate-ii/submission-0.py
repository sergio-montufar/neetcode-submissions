class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sliding_window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                sliding_window.remove(nums[left])
                left += 1

            if nums[right] in sliding_window:
                return True

            sliding_window.add(nums[right])

        return False