import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = np.zeros((m, n))
        dp[m-1, n-1] = 1 - obstacleGrid[m-1][n-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                dp1, dp2 = 0, 0
                if i+1 < m and obstacleGrid[i+1][j] == 0:
                    dp1 = dp[i+1, j]
                if j+1 < n and obstacleGrid[i][j+1] == 0:
                    dp2 = dp[i, j+1]
                dp[i, j] = dp1 + dp2
        return int(dp[0, 0])
        
