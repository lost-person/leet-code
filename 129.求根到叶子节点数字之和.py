#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0

        res = []
        def sum_numbers(node: TreeNode, tmp: str):
            if not node.left and not node.right:
                res.append(tmp)
                return
            
            if node.left:
                sum_numbers(node.left, tmp + str(node.left.val))
            
            if node.right:
                sum_numbers(node.right, tmp + str(node.right.val))

        sum_numbers(root, str(root.val))
        return sum(list(map(lambda x: int(x), res)))
# @lc code=end

