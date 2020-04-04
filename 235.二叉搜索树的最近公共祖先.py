#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p.val > q.val:
        #     p, q = q, p
        
        # def lowest_common_ancestor(node):
        #     if not node:
        #         return node
            
        #     if (p.val <= node.val and node.val < q.val) or (p.val < node.val and node.val <= q.val):
        #         return node
            
        #     left_root = lowest_common_ancestor(node.left)
        #     return left_root or lowest_common_ancestor(node.right)
        
        # return lowest_common_ancestor(root)

        while root:
            if root.val < q.val and root.val < p.val:
                root = root.right
            if root.val > q.val and root.val > p.val:
                root = root.left
            else:
                return root
        
# @lc code=end

