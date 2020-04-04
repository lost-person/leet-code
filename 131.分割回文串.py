#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        if not s: return res

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 获取字符串 s 内的所有为回文串的子串
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
        def backtrack(start, length, tmp=[]):
            if start == length:
                res.append(tmp[:])
                return
            
            for i in range(start, length):
                if not dp[start][i]:
                    continue
                
                backtrack(i + 1, length, tmp + [s[start: i + 1]])

        backtrack(0, n, [])
        return res 

# @lc code=end

