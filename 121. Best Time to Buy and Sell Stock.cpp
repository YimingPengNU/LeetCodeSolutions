class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty())
            return 0;     
        int runMin = prices[0];
        int res = 0;
        for (auto p : prices) {
            res = max(res, p - runMin);
            runMin = min(runMin, p);
        }
        return res;
    }
};
