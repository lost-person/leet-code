# coding = utf-8

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0

        n = len(nums)
        if n == 1:
            return 1

        for i in range(n):
            if nums[i] != i:
                return i
