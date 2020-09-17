#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        if not nums:
            return res

        n = len(nums)

        # gg 超时
        # for start in range(n):
        #     tmp_sum = 0
        #     for end in range(start, n):
        #         tmp_sum += nums[end]
        #         if tmp_sum == k:
        #             res += 1

        sum_dict = dict()
        sum_dict[0] = 1
        tmp_sum = 0
        for i in range(n):
            tmp_sum += nums[i]
            if (tmp_sum - k) in sum_dict:
                res += sum_dict.get(tmp_sum - k)

            sum_dict[tmp_sum] = sum_dict.get(tmp_sum, 0) + 1

        return res


# @lc code=end
