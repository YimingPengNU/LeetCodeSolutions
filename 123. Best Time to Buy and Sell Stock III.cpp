using vec = vector<int>;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty())
            return 0;
        
        vec res1 = maxProfitOne(prices);
        int profit1 = res1[0];
        
        int profit2 = 0;
        if (res1[1] > 0) {
            vec pricesBefore(prices.begin(), prices.begin() + res1[1]);
            vec res2 = maxProfitOne(pricesBefore);
            profit2 = res2[0];
        }
        
        int profit3 = 0;
        if (res1[2] < prices.size() - 1) {
            vec pricesAfter(prices.begin() + res1[2] + 1, prices.end());
            vec res3 = maxProfitOne(pricesAfter);
            profit3 = res3[0];
        }
           
        int drawdown = 0;
        if (res1[2] - res1[1] > 0) {
            vec pricesReversed(prices.begin() + res1[1], prices.begin() + res1[2] + 1);
            reverse(pricesReversed.begin(), pricesReversed.end());
            vec res4 = maxProfitOne(pricesReversed);
            drawdown = res4[0];
        }
        
        return max({profit1 + profit2, profit1 + profit3, profit1 + drawdown});
    }
    
    vec maxProfitOne(vec& prices) {
        vec res(3, 0);
        if (prices.size() > 1) {
            int currMin = prices[0];
            int profit = 0;
            int buyPt = 0;
            int sellPt = 0;
            int minPt = 0;
            for (int i = 1; i < prices.size(); i++) {
                int price = prices[i];
                if (price - currMin > profit)  {
                    buyPt = minPt;
                    sellPt = i;
                    profit = price - currMin;
                }
                if (price < currMin) {
                    minPt = i;
                    currMin = price;
                }
            res[0] = profit;
            res[1] = buyPt;
            res[2] = sellPt;
            }
        }
        return res;
    }
};
