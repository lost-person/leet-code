#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        if not n: return n

        # res = 0
        # for i in range(31, -1, -1):
        #     res |= ((n >> (31 - i) & 1) << i)
        # return res

        # 这个 c 的源码太强了
        n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16) # 前16位，与后16位交换，以下等价
        n = ((n & 0xff00ff00) >>  8) | ((n & 0x00ff00ff) <<  8) 
        n = ((n & 0xf0f0f0f0) >>  4) | ((n & 0x0f0f0f0f) <<  4) 
        n = ((n & 0xcccccccc) >>  2) | ((n & 0x33333333) <<  2) 
        n = ((n & 0xaaaaaaaa) >>  1) | ((n & 0x55555555) <<  1)
        return n
# @lc code=end

