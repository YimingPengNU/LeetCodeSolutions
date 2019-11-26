class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # if k is large enough s.t. we can capture every price increase
        if 2 * k > len(prices): 
            return sum(prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i])
        
        # dp table for max profit with at most i trades where 1 <= i <= k
        dp = [0] * (k+1) 
        # adjusted buy price taking in account of max profit earned with at most i-1 trades
        buy = [float('inf')] * (k+1) 
        for p in prices:
            for i in range(1, k+1):
                buy[i] = min((p - dp[i-1]), buy[i])
                dp[i] = max(dp[i], (p - buy[i]))
        return dp[k]
        
