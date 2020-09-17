#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        res = 0
        if not nums:
            return res

        # n = len(nums)

        # dp = [[0] * 2001 for _ in range(n)]
        # dp[0][nums[0] + 1000] = 1
        # dp[0][-nums[0] + 1000] += 1

        # for i in range(1, n):
        #     for j in range(-1000, 1001):
        #         if dp[i - 1][j + 1000] > 0:
        #             dp[i][j + 1000 + nums[i]] += dp[i - 1][j + 1000]
        #             dp[i][j + 1000 - nums[i]] += dp[i - 1][j + 1000]

        # return dp[n - 1][S + 1000] if S <= 1000 else 0

        # dp = [0] * 2001
        # dp[nums[0] + 1000] = 1
        # dp[-nums[0] + 1000] += 1
        # for i in range(1, n):
        #     tmp = [0] * 2001
        #     for j in range(-1000, 1001):
        #         if dp[j + 1000] > 0:
        #             tmp[j + 1000 + nums[i]] += dp[j + 1000]
        #             tmp[j + 1000 - nums[i]] += dp[j + 1000]
        #     dp = tmp[:]
        # return dp[S + 1000] if S <= 1000 else 0

        length = len(nums)
        if length == 0:
            return 0
        note = {}

        def get_res(ind, temp):
            if ind == length:
                if temp == 0:
                    return 1
                else:
                    return 0
            if (ind, temp) in note:
                return note[(ind, temp)]
            res = get_res(ind + 1, temp + nums[ind]) + get_res(
                ind + 1, temp - nums[ind])
            note[(ind, temp)] = res
            return res

        return get_res(0, S)


# @lc code=end
