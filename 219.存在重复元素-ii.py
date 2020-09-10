#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False
        
        n = len(nums)
        num_set = set()
        for i, num in enumerate(nums):
            if num in num_set: return True
            num_set.add(num)
            if len(num_set) > k: num_set.remove(nums[i - k])
        
        return False
# @lc code=end

