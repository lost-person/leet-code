#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        m, n = len(matrix), len(matrix[0])

        max_len, prev = 0, 0
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tmp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return max_len * max_len
# @lc code=end

