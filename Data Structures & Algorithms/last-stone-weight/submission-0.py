
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # in order to turn a min-heap to a max-heap
        # turn numbers to negatives, cuz python does not
        # have max-heap built-in, only min-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0) # if stones is empty because
                         # all stones are destroyed
        return abs(stones[0])