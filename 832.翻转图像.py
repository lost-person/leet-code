#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])

        for i in range(m):
            for j in range((n + 1) // 2):
                A[i][j], A[i][n - j - 1] = A[i][n - j - 1] ^ 1, A[i][j] ^ 1

        return A


# @lc code=end
