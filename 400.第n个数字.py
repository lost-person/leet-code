#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#

# @lc code=start


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 个位数 9 两位数 90 * 2 三位数 900 * 3
        if n < 10:
            return n

        base, bit, p = 9, 1, 0
        while n > base * bit:
            n -= base * bit
            base *= 10
            bit += 1
            p += 1

        p = pow(10, p)
        p += n // bit
        index = n % bit
        if index != 0:
            return int(str(p)[index - 1])
        else:
            return int(str(p - 1)[-1])


# @lc code=end
