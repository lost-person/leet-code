#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#


# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # 找到起始字符的最大回文子串，然后将剩余字符子串翻转补充到开头即可
        if not s or len(s) < 2:
            return s

        # # 翻转字符串，并添加到末尾，通过KMP算法查找最大部分匹配前缀
        # rev = s[::-1]
        # s_new = s + "#" + rev
        # n_new, n = len(s_new), len(s)

        # f_new = [0] * n_new
        # for i in range(1, n_new):
        #     t = f_new[i - 1]
        #     while t > 0 and s_new[i] != s_new[t]:
        #         t = f_new[t - 1]
        #     if s_new[i] == s_new[t]:
        #         t += 1
        #     f_new[i] = t

        # return rev[:n - f_new[n_new - 1]] + s

        # 马拉车算法 查询每个字符为中心的回文子串之后，找到包含开头字符的最大回文子串
        s_new = "#" + "#".join(s) + "#"
        n_new = len(s_new)
        p = [0] * n_new

        center, max_right = 0, 0
        for i in range(1, n_new):
            if i < max_right:
                mirror = 2 * center - i
                p[i] = min(p[mirror], max_right - i)

            while i + p[i] + 1 < n_new and i - p[i] - 1 >= 0 and s_new[
                    i + p[i] + 1] == s_new[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i

        # 寻找包含开头字符的最大回文子串
        if center == max_right:
            return s

        max_len = 0
        for i in range(1, n_new // 2 + 1):
            if i == p[i]:
                max_len = i

        return s[max_len:][::-1] + s


# @lc code=end
