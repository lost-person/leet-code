#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr: return 0

        n = len(arr)
        if n < 3: return 0

        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end
