#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if not haystack:
            return -1
        
        m, n = len(haystack), len(needle)
        next_list = [-1] * len(needle)
        
        def get_next(s: str):
            i, j = -1, 0
            while j < n - 1:
                if i == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    if s[i] == s[j]:
                        next_list[j] = next_list[i]
                    else:
                        next_list[j] = i
                else:
                    i = next_list[i]
        
        get_next(needle)
        
        i, j = 0, 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_list[j]
        return i - j if j == n else -1
# @lc code=end

