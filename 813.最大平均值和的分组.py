#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#

# @lc code=start
from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)

        prefix = [0]
        for num in A:
            prefix.append(prefix[-1] + num)

        def average(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        dp = [average(i, n) for i in range(n)]

        for _ in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]


# @lc code=end
