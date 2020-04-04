#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if not len(nums): return res
        
        def backtrack(nums, tmp):
            if not len(nums):
                res.append(tmp)
                return 
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res
# @lc code=end

