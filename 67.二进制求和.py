#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ''

        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        carry = 0
        while i >= 0 and j >= 0:
            tmp_sum = carry + int(a[i]) + int(b[j])
            carry = tmp_sum // 2
            tmp_sum = str(tmp_sum % 2)
            # 有无进位
            s = tmp_sum + s
            i -= 1
            j -= 1

        if i < 0:
            while j >= 0:
                tmp_sum = int(b[j]) + carry
                carry = tmp_sum // 2
                tmp_sum = str(tmp_sum % 2)
                s = tmp_sum + s
                j -= 1
        else:
            while i >= 0:
                tmp_sum = int(a[i]) + carry
                carry = tmp_sum // 2
                tmp_sum = str(tmp_sum % 2)
                s = tmp_sum + s
                i -= 1

        if carry:
            s = '1' + s
        return s


# @lc code=end
