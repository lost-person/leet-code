# coding = utf-8

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return -1

        once, twice = 0, 0
        for num in nums:
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)

        return once
