#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums = sorted(nums)
        # res = [[], [nums[0]]]
        # size_before = 1

        # for i in range(1, len(nums)):
        #     size = len(res)
        #     if nums[i] != nums[i - 1]:
        #         size_before = size
        #     for subres in res[size - size_before:size]:
        #         res.append(subres + [nums[i]])
        # return res

        num_dict = dict()
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        res = [[]]
        for k, v in num_dict.items():
            for subres in res[:]:
                for i in range(v):
                    res.append(subres + [k] * (i + 1))

        return res


# @lc code=end
