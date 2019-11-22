class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        dp = [[0] * N for _ in range(N)]
        dp[N-1] = A[N-1]
        for i in range(N-2, -1, -1):
            for j in range(N):
                dp[i][j] = A[i][j] + min(dp[i+1][max(0, j-1)], dp[i+1][j], dp[i+1][min(N-1,j+1)])
        return min(dp[0])
        
