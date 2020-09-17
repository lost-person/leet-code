#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return n
        # mask = 1
        # res = 0
        # for i in range(32):
        #     if n & mask:
        #         res += 1
        #     mask <<= 1
        # return res

        # n二进制表示的最后一个 1 一定是 n - 1 的0
        # 因此 n & (n - 1) 一定会把 n 最后一个 1 置为 0，而其他不变
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res


# @lc code=end
