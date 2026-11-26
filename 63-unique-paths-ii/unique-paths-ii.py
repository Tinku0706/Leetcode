class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1 for j in range(n)] for i in range(m)]
        return self.UniqueGrid2(m-1,n-1,obstacleGrid,dp)
    def UniqueGrid2(self,i,j,obstacleGrid,dp):
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=self.UniqueGrid2(i-1,j,obstacleGrid,dp)+self.UniqueGrid2(i,j-1,obstacleGrid,dp)
            return dp[i][j]
        