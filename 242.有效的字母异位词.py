#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        if not m: return True
        
        alpha_list = [0] * 26
        for i in range(m):
            alpha_list[ord(s[i]) - 97] += 1
            alpha_list[ord(t[i]) - 97] -= 1
        
        if any(alpha_list): return False
        return True
# @lc code=end

