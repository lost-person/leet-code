#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # 增加虚拟气球
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                max_profit = 0
                for k in range(i + 1, j):
                    tmp = dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    max_profit = max(tmp, max_profit)
                dp[i][j] = max_profit

        return dp[0][n - 1]


# @lc code=end
