#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = float('-inf')
        imax, imin = 1, 1

        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            res = max(res, imax)
        
        return res
# @lc code=end

