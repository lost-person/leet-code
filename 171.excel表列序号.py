#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0
        
        res = 0
        for c in s:
            res = res * 26 + ord(c) - 64
        return res
# @lc code=end

