class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty())
            return 0;
        int sumProfit = 0;
        int profit = 0;
        int lastPrice = prices[0];
        for (auto p : prices) {
            if (p > lastPrice) 
                profit += p - lastPrice;
            if (p < lastPrice) {
                sumProfit += profit;
                profit = 0;
            }
            lastPrice = p;
        }
        sumProfit += profit;
        return sumProfit;
    }
};
