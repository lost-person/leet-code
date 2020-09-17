#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root: return True, -1

            left_balanced, left_height = height(root.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_height = height(root.right)
            if not right_balanced:
                return False, 0

            return abs((left_height -
                        right_height)) < 2, max(left_height, right_height) + 1

        return height(root)[0]


# @lc code=end
