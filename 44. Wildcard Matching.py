class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M = len(p)
        N = len(s)  
        
        # empty pattern can only match empty string
        if M == 0:
            return N == 0 
        
        dp = [[0] * (M+1) for _ in range(N+1)]
        # empty pattern can match empty string
        dp[0][0] = 1
            
        # for empty string
        for j in range(1, M+1):
            # if j-th char in pattern is * then it is a match
            if p[j-1] == '*': 
                dp[0][j] = dp[0][j-1]
        
        # for nonempty string and nonempty pattern
        for i in range(1, N+1):
            for j in range(1, M+1):
                # If current characters match, result is same as 
                # result for lengths minus one. Characters match
                # in two cases:
                # a) If pattern character is '?' then it matches  
                #    with any character of text. 
                # b) If current characters in both match
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                # If we encounter ‘*’, two choices are possible-
                # a) We ignore ‘*’ character and move to next 
                #    character in the pattern, i.e., ‘*’ 
                #    indicates an empty sequence.
                # b) '*' character matches with ith character in input 
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                # if (p[j – 1] != s[i - 1])
                else:
                    dp[i][j] = 0
        
        return dp[N][M] == 1
