#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals: return [newInterval]
        if not newInterval: return intervals

        n = len(intervals)
        idx = 0
        while idx < n and intervals[idx][0] <= newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        if idx:
            intervals = [newInterval] + intervals[idx:]
        else:
            res.append(newInterval)

        for interval in intervals:
            if res[-1][1] >= interval[0]:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
            else:
                res.append(interval)
        return res


# @lc code=end
