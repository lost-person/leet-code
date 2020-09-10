#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if not s:
            return res
        
        m, n = len(s), len(p)
        if m < n:
            return res
        
        alpha_list = [0] * 26
        for p_c in p:
            alpha_list[ord(p_c) - ord('a')] += 1
        
        left, right = 0, n - 1
        for i in range(left, right + 1):
            alpha_list[ord(s[i]) - ord('a')] -= 1
        
        if not any(alpha_list):
            res.append(left)

        while right < m - 1:
            alpha_list[ord(s[left]) - ord('a')] += 1
            left += 1
            right += 1
            alpha_list[ord(s[right]) - ord('a')] -= 1
            if not any(alpha_list):
                res.append(left)
        return res
# @lc code=end

