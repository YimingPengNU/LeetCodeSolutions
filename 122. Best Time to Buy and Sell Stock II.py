class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len( prices) <= 1:
            return 0
        profit = 0
        last = prices[0]
        for price in prices[1:]:
            profit += max(0, price - last)
            last = price
        return profit
            
        
