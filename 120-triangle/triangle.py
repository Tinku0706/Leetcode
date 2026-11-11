class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[[1]*n for _ in range(n)]
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                diagonal_up=dp[i-1][j-1] if j>0 else float('inf')
                up=dp[i-1][j] if j<len(triangle[i-1]) else float('inf')
                dp[i][j]=triangle[i][j]+min(diagonal_up,up)
        return min(dp[n-1])
        