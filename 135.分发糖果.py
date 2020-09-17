#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 向左向右看，两次遍历
        # res = 0
        # if not ratings: return res

        # n = len(ratings)
        # dp = [1] * n

        # for i in range(1, n):
        #     if ratings[i] > ratings[i - 1]:
        #         dp[i] = dp[i - 1] + 1

        # for i in range(n - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1]:
        #         dp[i] = max((dp[i], dp[i + 1] + 1))
        # return sum(dp)

        if not ratings: return 0
        n = len(ratings)
        if len(ratings) < 2: return n

        def count(n):
            return (n * (n + 1)) >> 1

        candies = 0
        up, down, old_slope = 0, 0, 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            elif ratings[i] < ratings[i - 1]:
                new_slope = -1
            else:
                new_slope = 0

            if (old_slope > 0 and new_slope == 0) or (old_slope < 0
                                                      and new_slope >= 0):
                candies += count(up) + count(down) + max(up, down)
                up = 0
                down = 0

            if new_slope > 0:
                up += 1

            if new_slope < 0:
                down += 1

            if new_slope == 0:
                candies += 1

            old_slope = new_slope

        candies += count(up) + count(down) + max(up, down) + 1
        return candies


# @lc code=end
