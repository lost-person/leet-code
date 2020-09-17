#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A or len(A) == 0: return []

        n = len(A)
        if n == 1: return [A[0]**2]

        res = []

        j = 0
        i, j = 0, n - 1
        while i < j:
            mid = i + (j - i) // 2
            if A[mid] < 0:
                i = mid + 1
            else:
                j = mid

        i, j = i - 1, j

        while 0 <= i and j < n:
            i_square = A[i]**2
            j_square = A[j]**2
            if i_square < j_square:
                res.append(i_square)
                i -= 1
            else:
                res.append(j_square)
                j += 1

        while 0 <= i:
            res.append(A[i]**2)
            i -= 1

        while j < n:
            res.append(A[j]**2)
            j += 1

        return res


# @lc code=end
