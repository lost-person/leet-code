#
# @lc app=leetcode.cn id=1283 lang=python3
#
# [1283] 使结果不超过阈值的最小除数
#

# @lc code=start
import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums or threshold == 0: return 0

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2
            tmp = sum([math.ceil(num / mid) for num in nums])
            if tmp > threshold:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

