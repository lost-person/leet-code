#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        def _rob(node):
            if not node:
                return [0, 0]
        
            left_res = _rob(node.left)
            right_res = _rob(node.right)

            res = [0, 0]
            res[0] = max(left_res[0], left_res[1]) + max(right_res[0], right_res[1])
            res[1] = left_res[0] + right_res[0] + node.val

            return res
        
        return max(_rob(root))

# @lc code=end

