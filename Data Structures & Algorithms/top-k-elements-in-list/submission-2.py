class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
     




        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # arr = []
        # for num, c in count.items():
        #    arr.append([c, num])
        # arr.sort()

        # ans = []
        # print(arr)
        # while len(ans) < k:
        #     ans.append(arr.pop()[1])
        

        # return ans
        