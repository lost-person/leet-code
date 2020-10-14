#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def recur(node: TreeNode):
            if not node: return False
            
            left_res = recur(node.left)
            right_res = recur(node.right)
            
            if not left_res: node.left = None
            if not right_res: node.right = None

            return node.val == 1 or left_res or right_res
            
        return root if recur(root) else None
# @lc code=end

