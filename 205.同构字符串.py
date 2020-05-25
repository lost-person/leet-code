#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_dict = {}
        for i in range(len(s)):
            if s[i] not in char_dict:
                if t[i] in char_dict.values():
                    return False
                else:
                    char_dict[s[i]] = t[i]
            else:
                if char_dict[s[i]] != t[i]:
                    return False
        return True
# @lc code=end

