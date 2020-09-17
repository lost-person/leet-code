#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        while root:
            if root.left:
                prev = root.left
                while prev and prev.right:
                    prev = prev.right

                prev.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


# @lc code=end
