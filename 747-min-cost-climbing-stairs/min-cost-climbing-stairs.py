class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[-1]*n
        return min(self.Helper(n-1,cost,dp),(self.Helper(n-2,cost,dp)))
    def Helper(self,i,cost,dp):
        if i==0 or i==1:
            return cost[i]
        if i<0:
            return 0
        if dp[i]!=-1:
            return dp[i]
        one=cost[i]+self.Helper(i-1,cost,dp)
        two=cost[i]+self.Helper(i-2,cost,dp)
        dp[i]=min(one,two)
        return dp[i]
        
        