class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        dp = [[False] * len(s) for _ in range(len(s))]
        for k in range(len(s)):
            for i in range(len(s) - k):
                j = i + k
                if k < 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        
        for k in range(len(s)-1, -1, -1):
            for i in range(len(s) - k):
                j = i + k
                if dp[i][j]:
                    return s[i:(j+1)]
        
