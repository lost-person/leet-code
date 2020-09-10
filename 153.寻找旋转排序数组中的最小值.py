#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
# @lc code=end
