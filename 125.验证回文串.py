#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1: return True

        s_new = ''
        for c in s:
            if c.isalnum():
                s_new += c.lower()
        
        mid = len(s_new) >> 1
        for i in range(mid):
            if s_new[i] != s_new[len(s_new) - i - 1]:
                return False
        
        return True
        
# @lc code=end

