#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        
        # def backtrack(nums, tmp):
        #     if len(tmp) == k:
        #         res.append(tmp[:])
        #         return
            
        #     for i in range(len(nums)):
        #         tmp.append(nums[i])
        #         backtrack(nums[i + 1:], tmp)
        #         tmp.pop()
        
        # k = 0
        # while k <= len(res):
        #     backtrack(nums, [])
        #     k += 1
        # return res
        res = [[]]
        for i in range(len(nums)):
            for subres in res[:]: res.append(subres+[nums[i]])
    
        return res
        
# @lc code=end

