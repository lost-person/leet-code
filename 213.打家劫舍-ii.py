#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n: return 0
        if n <= 2: return max(nums)

        def _rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(_rob(nums[1:]), _rob(nums[:-1]))


# @lc code=end
