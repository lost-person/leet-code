#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0: return 0

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]


# @lc code=end
