#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#


# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s:
            return int(not t)

        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j > i:
                    continue
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]

        # dp = [0] * (n + 1)
        # dp[0] = 1

        # c_dict = dict()
        # nexts = [0] * n
        # for i in range(n):
        #     c = t[i]
        #     nexts[i] = c_dict.get(c, -1)
        #     c_dict[c] = i

        # for i in range(m):
        #     c = s[i]
        #     j = c_dict.get(c, -1)
        #     while j >= 0:
        #         dp[j + 1] += dp[j]
        #         j = nexts[j]

        # return dp[n]


# @lc code=end
