class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2  # middle value
            totalTime = 0 # hours it takes to eat all piles in h time
            for p in piles:
                # p / k is the rate of piles we can eat per hour 
                # while math.ciel() function rounds UP to the nearest number
                totalTime += math.ceil(p / k) 

            if totalTime <= h:
                result = min(result, k)
                right = k - 1 # rate is big enough, but perhaps we can find smaller
            else:
                left = k + 1  # rate is too small, we need bigger a rate to eat all
        return result