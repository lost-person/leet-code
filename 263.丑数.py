#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#


# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        if num <= 6:
            return True

        n = num
        while n % 2 == 0:
            n /= 2

        while n % 3 == 0:
            n /= 3

        while n % 5 == 0:
            n /= 5

        return n == 1


# @lc code=end
