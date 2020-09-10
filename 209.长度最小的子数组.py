#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not s:
            return 0
        
        n = len(nums)
        res, cur_sum, left = n + 1, 0, 0
        
        for i, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= s:
                res = min(res, i - left + 1)
                cur_sum -= nums[left]
                left += 1
        return res if res < n + 1 else 0
# @lc code=end

