class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the max profit and buy/sell days with one transaction
        profit1, buyPt, sellPt = self.maxProfitOne(prices)
        # find the max profit in days before buy day of profit 1 with one transaction
        profit2, _, _ = self.maxProfitOne(prices[0:buyPt])
        # find the max profit in days after sell day of profit 1 with one transaction
        profit3, _, _ = self.maxProfitOne(prices[sellPt+1:])
        # find the max drawdown with buy/sell days of profit 1
        drawdown, _, _ = self.maxProfitOne(list(reversed(prices[buyPt:(sellPt+1)])))
        return max(profit1 + profit2, profit1 + profit3, profit1 + drawdown)
    
    def maxProfitOne(self, prices):
        '''find the max profit with one transaction
            return maxProft, buyPoint, sellPoint
        '''
        if len(prices) <= 1:
            return 0, 0, 0
        currMin = prices[0]
        profit = 0
        buyPt = 0
        sellPt = 0
        minPt = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price - currMin > profit:
                buyPt = minPt
                sellPt = i
                profit = price - currMin
            if price < currMin:
                minPt = i
                currMin = price    
        return profit, buyPt, sellPt
