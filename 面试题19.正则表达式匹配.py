# coding = utf-8

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(n):
            if dp[0][j - 1] and p[j] == '*':
                dp[0][j + 1] = True

        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    if p[j] == '*':
                        if s[i] != p[j - 1] and p[j - 1] != '.':
                            dp[i + 1][j + 1] = dp[i + 1][j - 1]
                        else:
                            dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[m][n]

