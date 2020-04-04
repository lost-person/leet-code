#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        # dp
        # n = len(s)
        # res = 0
        # dp = [[False] * n for _ in range(n)]
        
        # for i in range(n):
        #     for j in range(i, -1, -1):
        #         if s[i] == s[j] and (i - j + 1 <= 2 or dp[i-1][j+1]):
        #             dp[i][j] = True
        #             res += 1
        # return res

        # 中心扩展
        # for center in range(2 * n - 1):
        #     left = center // 2
        #     right = left + center % 2
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         res += 1
        #         left -= 1
        #         right += 1
        
        # return res
        
        # 马拉车算法
        s = "#" + "#".join(s) + "#"
        n = len(s)
        p = [0] * n

        center, max_right = 0, 0
        for i in range(1, n):
            if i < max_right:
                mirror = 2 * center - i
                p[i] = min(p[mirror], max_right - i)
            
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
        
        return sum((p_i + 1) >> 1 for p_i in p)
        
# @lc code=end

