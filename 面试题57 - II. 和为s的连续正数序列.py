# coding = utf-8

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        if target < 3:
            return res

        left, right = 1, 2
        while left < right:
            cur_sum = ((right - left + 1) * (left + right)) >> 1
            if cur_sum == target:
                res.append(list(range(left, right + 1)))
                left += 1
            elif cur_sum < target:
                right += 1
            else:
                left += 1

        return res
