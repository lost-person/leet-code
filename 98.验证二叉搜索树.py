#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def is_validBST(node, low_value=float('-inf'), high_value=float('inf')):
        #     if not node: return True

        #     if node.val <= low_value or node.val >= high_value:
        #         return False
            
        #     if not is_validBST(node.left, low_value, node.val):
        #         return False
            
        #     if not is_validBST(node.right, node.val, high_value):
        #         return False
            
        #     return True

        # return is_validBST(root)

        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
# @lc code=end

