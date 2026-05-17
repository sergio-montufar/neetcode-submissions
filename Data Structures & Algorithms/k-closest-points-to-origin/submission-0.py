class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        # compute squared distance from origin
        for x, y in points:
            # d = sqrt((x1 - x2)^2 +(y1-y2)^2)
            distance = -(x**2 + y**2) # negative becuz max-heap
            heapq.heappush(max_heap, [distance, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []
        while max_heap:
            dist, x, y = heapq.heappop(max_heap)
            result.append([x, y])
        
        return result

        
