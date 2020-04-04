#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for word in path.split('/'):
            if word not in ['', '.', '..']:
                stack.append(word)
            elif word == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)
# @lc code=end

