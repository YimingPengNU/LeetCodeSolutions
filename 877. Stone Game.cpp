class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        // base case
        int N = piles.size();
        if (N < 3)
            return true;
        int partialSums[N][N];
        for (int i = 0; i < N; i++) {
            int partialSum = 0;
            for (int j = i; j < N; j++) {
                partialSum += piles[j];
                partialSums[i][j] = partialSum;
            }
        }
        int dp[N][N];
        for (int i = 0; i < N-1; i++) {
            dp[i][i] = piles[i];
            dp[i][i+1] = max(piles[i], piles[i+1]);
        }
        for (int j = 2; j < N; j++) {
            for (int i = 0; i < N-j; i++) {
                dp[i][i+j] = partialSums[i][i+j] - min(dp[i+1][i+j], dp[i][i+j-1]);
            }
        }
        int totalSum = partialSums[0][N-1];
        return (dp[0][N-1] > int(totalSum/2))? true : false;
    }
};
