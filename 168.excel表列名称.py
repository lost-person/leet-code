#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#


# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""

        while n:
            n -= 1
            res += chr(n % 26 + 65)
            n //= 26

        return res[::-1]


# @lc code=end
