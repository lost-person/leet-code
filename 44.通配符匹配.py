#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            匹配成功：
                1): p[i] == s[j] or p[i] == "?
                2): p[i] == "*"
                    a) * 为空
                    b) * 匹配 s[j]
        """
        n, m = len(p), len(s)
        res = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        res[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == "*": res[i][0] = True
            else: break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    res[i][j] = res[i - 1][j - 1]
                elif p[i - 1] == '*':
                    res[i][j] = res[i - 1][j] or res[i][j - 1]
                else:
                    res[i][j] = False

        return res[n][m]


# @lc code=end
