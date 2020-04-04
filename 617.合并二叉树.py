#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        
        # def merge_trees(node, node1, node2):
        #     if not node1 and not node2:
        #         return None
        #     elif node1 and not node2:
        #         return node1
        #     elif not node1 and node2:
        #         return node2
        #     node.val = node1.val + node2.val
        #     node.left = merge_trees(TreeNode(0), node1.left, node2.left)
        #     node.right = merge_trees(TreeNode(0), node1.right, node2.right)
        #     return node
        # t = merge_trees(TreeNode(0), t1, t2)
        # return t

        if not t1:
            return t2
        
        stack = []
        stack.append((t1, t2))
        while stack:
            t_0, t_1 = stack.pop()
            if not t_0 or not t_1:
                continue
            t_0.val += t_1.val
            if not t_0.left:
                t_0.left = t_1.left
            else:
                stack.append((t_0.left, t_1.left))
            if not t_0.right:
                t_0.right = t_1.right
            else:
                stack.append((t_0.right, t_1.right))
        
        return t1
# @lc code=end

