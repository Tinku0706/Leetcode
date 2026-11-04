class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        return max(self.solve(nums[:-1]),self.solve(nums[1:]))
    
    def solve(self,nums):
        prev1=0
        prev2=0
        for i in nums:
            cur=max(prev2+i,prev1)

            prev2=prev1
            prev1=cur
        return prev1    
        
        
        