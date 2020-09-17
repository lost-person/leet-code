#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#


# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"

        frac = ''
        if (numerator < 0) ^ (denominator < 0):
            frac += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)
        frac += str(numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return frac

        frac += '.'
        remainder_dict = dict()
        while remainder != 0:
            if remainder in remainder_dict.keys():
                frac = frac[:remainder_dict.get(remainder)] + "(" + frac[
                    remainder_dict.get(remainder):] + ")"
                break
            remainder_dict[remainder] = len(frac)
            remainder *= 10
            frac += str(remainder // denominator)
            remainder %= denominator
        return frac


# @lc code=end
