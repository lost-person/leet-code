#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
import math
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        res = 0
        i = 1
        while i <= n: # 依次统计个位，十位，百位上的1
            a = n // i
            b = n % i
            res += (a + 8) // 10 * i + (a % 10 == 1) * (b + 1)
            i *= 10
        return res

# @lc code=end

