#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#

# @lc code=start
from typing import List 

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        if n == 1:
            return A

        for i in range(n - 1, 0, -1):
            if A[i - 1] <= A[i]: continue

            for j in range(n - 1, i - 1, -1):
                if A[j] < A[i - 1]:
                    A[i - 1], A[j] = A[j], A[i - 1]
                    return A
        
        return A
# @lc code=end

