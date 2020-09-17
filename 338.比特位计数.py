#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # 191 扩展
        res = [0]
        if not num:
            return res

        # def count_bit(n: int):
        #     cnt = 0
        #     while n:
        #         cnt += 1
        #         n &= n - 1
        #     return cnt

        # for i in range(1, num + 1):
        #     res.append(count_bit(i))
        # return res

        # dp + 最高有效位
        # dp[i + b] = dp[i] + 1, b = 2^m > i
        # i = 0
        # b = 1
        # res = [0] * (num + 1)
        # while b <= num:
        #     while i < b and i + b <= num:
        #         res[i + b] = res[i] + 1
        #         i += 1
        #     i = 0
        #     b <<= 1
        # return res

        # dp + 最低有效位
        # dp[x] = dp[x / 2] + (x mod 2)
        # res = [0] * (num + 1)
        # for i in range(1, num + 1):
        #     res[i] = res[i >> 1] + (i & 1)
        # return res

        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i & (i - 1)] + 1
        return res


# @lc code=end
