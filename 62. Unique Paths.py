import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = np.zeros((m, n))
        dp[m-1, n-1] = 1
        dp[m-1, 0:(n-1)] = 1
        dp[0:(m-1), n-1] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i, j] = dp[i+1, j] + dp[i, j+1]
        return int(dp[0, 0])
        
        
