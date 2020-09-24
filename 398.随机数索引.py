#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start
import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        index = 0
        cnt = 0
        nums = self.nums

        for i, num in enumerate(nums):
            if num == target:
                cnt += 1
                sample = random.randint(1, cnt)
                if sample == cnt:
                    index = i

        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

