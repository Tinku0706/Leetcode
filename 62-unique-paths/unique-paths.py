class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for j in range(n)] for i in range(m)]
        return self.UniqueGrid(m-1,n-1,dp)
    def UniqueGrid(self,i,j,dp):
       if i==0 and j==0:
        return 1
       if i<0 or j<0:
        return 0
       if dp[i][j]!=-1:
        return dp[i][j]
       dp[i][j]=self.UniqueGrid(i,j-1,dp)+self.UniqueGrid(i-1,j,dp)
       return dp[i][j]