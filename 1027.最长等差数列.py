#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#

# @lc code=start
from typing import List

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        if not A: return res

        n = len(A)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = 2

        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         target = 2 * A[i] - A[j]
        #         for k in range(i - 1, -1, -1):
        #             if A[k] == target:
        #                 dp[i][j] = dp[k][i] + 1
        #                 break
        #         res = max(res, dp[i][j])

        # return res

        tmp_list = [-1] * 1001
        for i in range(n - 1):
            for j in range(i + 1, n):
                target = 2 * A[i] - A[j]
                if target < 0: continue
                if tmp_list[target] != -1: dp[i][j] = dp[tmp_list[target]][i] + 1
                res = max(res, dp[i][j])
            
            tmp_list[A[i]] = i
        return res
# @lc code=end

