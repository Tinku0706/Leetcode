class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[[-1]*n for _ in range(n)]

        return min(self.Triangle(n-1,j,triangle,dp) for j in range(n))

    def Triangle(self,i,j,triangle,dp):

        if i==0 and j==0:
            return triangle[0][0]

        if i<0 or j<0 or j>=len(triangle[i]):
            return float('inf')

        if dp[i][j]!=-1:
            return dp[i][j]

        diagonal_up=self.Triangle(i-1,j-1,triangle,dp)
        up=self.Triangle(i-1,j,triangle,dp)

        dp[i][j]=triangle[i][j]+min(diagonal_up,up)

        return dp[i][j]