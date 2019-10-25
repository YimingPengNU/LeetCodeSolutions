class Solution {
public:
    int numSquares(int n) {
        //largest k such that k*k <= n
        int k = int(sqrt(n));
        vector<int> squares(k, 0);
        for (int i = 0; i < k; i++) {
            squares[i] = (i+1)*(i+1);
        }
        vector<int> dp(n+1,0);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            int min = i;
            for (int j:squares) {
                if ((i - j >= 0) && dp[i - j] + 1 < min)
                    min = dp[i - j] + 1;
            }
            dp[i] = min;
        }
        return dp[n];
    }
};
