class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        dp=[[0]*n for _ in range(n)]
        dp[0]=matrix[0]
        for i in range(1,n):
            for j in range(n):
                left=dp[i-1][j-1] if j>0 else float('inf')
                up=dp[i-1][j]
                right=dp[i-1][j+1] if j<n-1 else float('inf')
                dp[i][j]=matrix[i][j]+min(left,up,right)
        return min(dp[n-1])        