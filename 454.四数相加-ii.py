#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        sum_dict = dict()
        res = 0

        for num_a in A:
            for num_b in B:
                tmp_sum = num_a + num_b
                sum_dict[str(tmp_sum)] = sum_dict.get(str(tmp_sum), 0) + 1

        for num_c in C:
            for num_d in D:
                tmp_sum = -(num_c + num_d)
                res += sum_dict.get(str(tmp_sum), 0)
        return res


# @lc code=end
