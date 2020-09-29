#
# @lc app=leetcode.cn id=1007 lang=python3
#
# [1007] 行相等的最少多米诺旋转
#

# @lc code=start
from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B: return -1

        m, n = len(A), len(B)
        if m != n or m == n == 0: return -1

        if m == 1: return 0

        def check(x: int):
            rotations_a = rotations_b = 0
            for i in range(m):
                if A[i] != x and B[i] != x: return -1
                elif A[i] != x:
                    rotations_a += 1
                elif B[i] != x:
                    rotations_b += 1
            
            return min(rotations_a, rotations_b)

        rotations = check(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return check(B[0])
# @lc code=end

