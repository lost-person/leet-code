#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        if not A or len(A) < 2: return 0

        n = len(A)

        max_num, left_max_num = A[0], A[0]
        left = 0
        
        for i in range(1, n):
            max_num = max(max_num, A[i])
            if left_max_num <= A[i]: continue

            left_max_num = max_num
            left = i
        return left + 1


# @lc code=end
