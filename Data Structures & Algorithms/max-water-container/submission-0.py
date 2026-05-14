class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0

        while left < right:
            max_water = (right - left) * min(heights[left], heights[right])
            ans = max(max_water, ans)
            print(left, right)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        

        return ans

        