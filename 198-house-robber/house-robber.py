class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[-1]*len(nums)
        return self.Helper(len(nums)-1,nums,dp)
    def Helper(self,i,nums,dp):
        if i<0:
            return 0
        if i==0:
            return nums[0]
        if dp[i]!=-1:
            return dp[i]
        pick=nums[i]+self.Helper(i-2,nums,dp)
        notpick=self.Helper(i-1,nums,dp)
        dp[i]=max(pick,notpick)
        return dp[i]
        