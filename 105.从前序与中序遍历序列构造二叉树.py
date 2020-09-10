#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder: return None

        pre_idx = 0
        def build_tree(left, right):
            nonlocal pre_idx
            if left == right:
                return None
            
            val = preorder[pre_idx]
            root = TreeNode(val)
            
            pre_idx += 1
            in_index = inorder.index(val)
            root.left = build_tree(left, in_index)
            root.right = build_tree(in_index + 1, right)
            
            # 构建子树
            return root
        
        return build_tree(0, len(preorder))

# @lc code=end

