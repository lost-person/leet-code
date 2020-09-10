#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None

        def build_tree(left, right):
            
            if left > right: return None

            val = postorder.pop()
            root = TreeNode(val)

            in_idx = inorder.index(val)
            
            root.right = build_tree(in_idx + 1, right)
            root.left = build_tree(left, in_idx - 1)
            
            return root
        
        return build_tree(0, len(postorder) - 1)
# @lc code=end

