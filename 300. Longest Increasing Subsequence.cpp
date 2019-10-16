class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty())
            return 0;        
        int INF = 1 << 20;
        vector<int> dp(nums.size(), INF);
        dp[0] = nums[0];
        for (auto i = 1; i < nums.size(); ++i) {
            int k = lower_bound(dp.begin(), dp.end(), nums[i]) - dp.begin();
            if (k < dp.size())
                dp[k] = nums[i];               
        }
        int res = 0;
        for (auto i = 0; i < dp.size(); ++i) {
            if (dp[i] < INF)
                res++;
        }
        return res;
    }
};
