#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))

        res = []

        def backtrack(nums, tmp):
            if len(tmp) == k:
                res.append(tmp[:])
                return

            for i in range(len(nums)):
                tmp.append(nums[i])
                backtrack(nums[i + 1:], tmp)
                tmp.pop()

        backtrack(nums, [])
        return res

        # init first combination
        # nums = list(range(1, k + 1)) + [n + 1]

        # output, j = [], 0
        # while j < k:
        #     # add current combination
        #     output.append(nums[:k])
        #     # increase first nums[j] by one
        #     # if nums[j] + 1 != nums[j + 1]
        #     j = 0
        #     while j < k and nums[j + 1] == nums[j] + 1:
        #         nums[j] = j + 1
        #         j += 1
        #     nums[j] += 1

        # return output


# @lc code=end
