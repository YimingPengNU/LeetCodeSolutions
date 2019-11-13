class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        currMin = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price - currMin)
            currMin = min(currMin, price)
        return profit
        
