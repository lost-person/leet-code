#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or sum(nums) % k != 0: return False

        div = sum(nums) // k

        nums.sort()
        if nums[-1] > div: return False
        
        while nums and nums[-1] == div:
            nums.pop()
            k -= 1

        def search(groups):
            if not nums: return True

            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= div:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        return search([0] * k)
# @lc code=end

