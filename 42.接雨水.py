#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        left, right = 0, n - 1
        max_left, max_right = height[0], height[n - 1]

        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1
        return res
# @lc code=end

