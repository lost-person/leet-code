#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 排序(略)
        # hash表
        if not nums or len(nums) < 2:
            return False

        num_set = set(nums)
        if len(num_set) == len(nums):
            return False
        else:
            return True


# @lc code=end
