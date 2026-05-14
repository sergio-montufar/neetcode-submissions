class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            multiply = 1
            for j in range(len(nums)):
                if i != j:
                    multiply *= nums[j]
            
            ans.append(multiply)
        
        return ans
                    
        