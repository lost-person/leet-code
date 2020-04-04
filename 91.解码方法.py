#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        m = len(s)
        res = [0] * m
        if int(s[0]) == 0:
            res[0] = 0
        else:
            res[0] = 1
        if m == 1:
            return res[0]

        if int(s[1]) == 0:
            if 0 < int(s[0]) < 3:
                res[1] = res[0]
            else:
                res[1] = 0
        elif int(s[0]) == 0 or int(s[0]) > 2 or (int(s[0]) == 2 and int(s[1]) > 6):
            res[1] = res[0]
        else:
            res[1] = res[0] + 1
                
        for i in range(2, m):
            # 必须和前一字符共同解码
            if int(s[i]) == 0:
                if 0 < int(s[i - 1]) < 3:
                    res[i] = res[i - 2]
                else:
                    res[i] = 0
            # 单独解码
            elif int(s[i - 1]) == 0 or int(s[i - 1]) > 2 or (int(s[i - 1]) == 2 and int(s[i]) > 6):
                res[i] = res[i - 1]
            else:
                res[i] = res[i - 1] + res[i - 2]
        return res[m - 1]
# @lc code=end

