#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        
        if m > n:
            m, n = n, m
        
        # shift = 0

        # while m < n:
        #     m >>= 1
        #     n >>= 1
        #     shift += 1
        
        # return m << shift

        while m < n:
            n &= (n - 1)
        return n

# @lc code=end

