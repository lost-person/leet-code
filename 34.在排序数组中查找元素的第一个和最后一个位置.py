#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res_list = [-1,-1]
        res_list = self.search(nums, target, 0, len(nums) - 1, res_list)
        return res_list
    
    def search(self, nums: List[int], target: int, left: int, right: int, res_list: List[int]):
        if left > right:
            return res_list
        mid = left + (right - left) // 2
        if nums[mid] == target:
            res_list = [mid, mid]
            left_res_list = self.search(nums, target, left, mid - 1, res_list)
            right_res_list = self.search(nums, target, mid + 1, right, res_list)
            res_list[0] = left_res_list[0]
            res_list[1] = right_res_list[1]
        elif nums[mid] > target:
            res_list = self.search(nums, target, left, mid - 1, res_list)
        else:
            res_list = self.search(nums, target, mid + 1, right, res_list)
        return res_list

# @lc code=end
