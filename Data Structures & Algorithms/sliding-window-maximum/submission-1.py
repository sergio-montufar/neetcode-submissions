
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque() # contains indices
        l = r = 0

        while r < len(nums):
            # make sure no smaller values exist in deque
            # while smaller values exist, pop from deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if left value is out of bounds, remove from window
            if l > q[0]:
                q.popleft()

            # make sure window is at least size k
            if (r + 1) >= k:
                result.append(nums[q[0]]) # this is the maximum num
                # left increments to make sure window is size k
                l += 1  
                
            
            # right always increments by 1
            r += 1

        return result

        
        
        
        
        
        
        
        
        
        # res = []

        # left, right = 0, k
        # while right <= len(nums):
        #     max_num = max(nums[left:right])
        #     res.append(max_num)

        #     left += 1
        #     right += 1

        # return res

