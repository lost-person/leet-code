#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return res
        
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
           
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                res.append(i)
                
        return res

# @lc code=end

