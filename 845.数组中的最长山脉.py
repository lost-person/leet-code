#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

# @lc code=start
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = 0

        if not A: return res

        n = len(A)
        if n < 3: return res

        base = 0

        while base < n:
            end = base
            if end + 1 < n and A[end] < A[end + 1]:
                while end + 1 < n and A[end] < A[end + 1]:
                    end += 1

                if end + 1 < n and A[end] > A[end + 1]:
                    while end + 1 < n and A[end] > A[end + 1]:
                        end += 1

                    res = max(res, end - base + 1)

            base = max(end, base + 1)

        return res


# @lc code=end
