#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#

# @lc code=start
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        durations = [1, 7, 30]
        
        max_day = days[-1] + 1
        dp = [0] * (max_day)

        for day in range(1, max_day):
            if day in days:
                dp[day] = min(dp[max(0, day - 1)] + costs[0],
                                dp[max(0, day - 7)] + costs[1],
                                dp[max(0, day - 30)] + costs[2])
            else:
                dp[day] = dp[day - 1]
        
        return dp[-1]

# @lc code=end

