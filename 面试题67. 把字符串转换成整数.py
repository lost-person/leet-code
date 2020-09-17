# coding = utf-8


class Solution:
    def strToInt(self, str: str) -> int:
        res = 0
        s = str.strip()
        if not s:
            return res

        max_value = 2**31 - 1
        min_value = -(2**31)
        # 正负

        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] == '-' or s[0] == '+' else s

        for c in s:
            if c < '0' or c > '9':
                break

            num = int(c)
            if (max_value - num) // 10 < res:
                return max_value if sign == 1 else min_value

            res = res * 10 + num
        return sign * res
