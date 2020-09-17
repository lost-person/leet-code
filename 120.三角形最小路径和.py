#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return 0

        m, n = len(triangle), len(triangle[-1])
        dp = [0] * (n + 1)
        for i in range(m - 1, -1, -1):
            row_list = triangle[i]
            for j in range(len(row_list)):
                dp[j] = min(dp[j], dp[j + 1]) + row_list[j]

        return dp[0]


# @lc code=end
