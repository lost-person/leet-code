#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#

# @lc code=start
from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        if K == 0: return ans
        
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
        return ans


# @lc code=end
