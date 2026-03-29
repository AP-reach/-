class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty string matches empty pattern
        
        # Handle patterns with '*' that can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]  # '*' can match empty string
                
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':  # Match character or '?'
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # '*' can match empty string or one or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[m][n]
                    

                    



        