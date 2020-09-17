#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        if not s:
            return res

        roman_dict = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        prev_num = roman_dict.get(s[0])

        n = len(s)
        for i in range(1, n):
            num = roman_dict.get(s[i])
            if num > prev_num:
                res -= prev_num
            else:
                res += prev_num
            prev_num = num
        res += prev_num
        return res


# @lc code=end
