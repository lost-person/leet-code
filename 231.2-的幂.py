#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if not n:
        #     return False

        # while n & 1 == 0:
        #     n >>= 1
        # return n == 1
        return n > 0 and n & (n - 1) == 0


# @lc code=end
