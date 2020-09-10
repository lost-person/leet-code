#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1
        
        def depth(node: TreeNode):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            node_depth = max(left_depth, right_depth) + 1
            self.res = max(self.res, left_depth + right_depth + 1)
            return node_depth
        depth(root)
        return self.res - 1
# @lc code=end

