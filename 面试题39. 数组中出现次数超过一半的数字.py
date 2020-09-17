# coding = utf-8

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)
        if n <= 2:
            return nums[0]

        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if candidate == num else -1

        return candidate
