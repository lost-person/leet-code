#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 异或之后，参考 191
        xor = x ^ y
        res = 0
        while xor:
            # 与 1 与并移位
            # if xor & 1:
            #     res += 1
            # xor >>= 1
            res += 1
            xor = xor & (xor - 1)
        return res
# @lc code=end

