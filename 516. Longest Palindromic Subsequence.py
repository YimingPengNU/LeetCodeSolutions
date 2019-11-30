class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        dp = [[0] * len(s) for _ in range(len(s))]
        for k in range(len(s)):
            for i in range(len(s) - k):
                j = i + k
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if k > 1:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][len(s) -1]
                
            
        
