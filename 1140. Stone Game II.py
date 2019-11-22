from math import ceil

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = [[0] * (N+1) for i in range(N+1)]
        # dp[i][j] = maxNumStone(piles[i:], M)
        dp[N-1] = [piles[N-1]] * (N+1)
        for i in range(N-2, -1, -1):
            totalLeft = sum(piles[i:])
            for j in range(ceil((N-i)/2), N+1):
                dp[i][j] = totalLeft
            for j in range(1, ceil((N-i)/2)):
                maxNum = 0
                for X in range(1, 2*j+1):
                    maxNum = max(maxNum, totalLeft - dp[i+X][min(N, max(X, j))])
                dp[i][j] = maxNum
        return dp[0][1]
                
                
