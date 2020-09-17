#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        if n < 1: return 0
        if n == 1: return 1

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            guess_res = guess(mid)
            if guess_res == 0: return mid
            elif guess_res == 1: left = mid + 1
            else: right = mid


# @lc code=end
