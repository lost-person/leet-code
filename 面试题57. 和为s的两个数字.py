# coding = utf-8

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        if not nums:
            return res

        n = len(nums)
        if n < 2:
            return res

        low, high = 0, n - 1
        while low < high:
            cur_sum = nums[low] + nums[high]
            if cur_sum == target:
                res = [nums[low], nums[high]]
                return res
            elif cur_sum > target:
                high -= 1
            else:
                low += 1
        return res
