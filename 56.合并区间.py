#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res_list = []
        if not intervals: return res_list

        # 排序
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not res_list or interval[0] > res_list[-1][1]:
                res_list.append(interval)
            else:
                res_list[-1] = [
                    res_list[-1][0],
                    max(res_list[-1][1], interval[1])
                ]

        return res_list


# @lc code=end
