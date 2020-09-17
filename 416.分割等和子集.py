#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        n = len(nums)
        total_sum = sum(nums)
        if total_sum & 1 == 1:
            return False

        nums.sort()
        total_sum >>= 1

        # def can_partition(index: int, left: int, right):
        #     if left == 0 or right == 0:
        #         return True
        #     elif left < 0 or right < 0:
        #         return False
        #     else:
        #         return can_partition(index - 1, left - nums[index], right) or can_partition(index - 1, left, right - nums[index])

        # return can_partition(n - 1, total_sum, total_sum)

        dp = [False] * (total_sum + 1)
        dp[0] = True
        for i in range(n):
            for j in range(total_sum, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[-1]


# @lc code=end
