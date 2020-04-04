#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        
        g.sort()
        s.sort()

        res = 0
        m, n = len(g), len(s)
        i, j = 0, 0
        while i < m and j < n:
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
                res += 1
        return res
# @lc code=end

