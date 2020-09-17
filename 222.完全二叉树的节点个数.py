#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def compute_depth(node: TreeNode):
            d = 0
            while node.left:
                node = node.left
                d += 1

            return d

        def exists(node, d, pivot):
            left, right = 0, 2**d - 1
            for _ in range(d):
                mid = left + (right - left) // 2
                if pivot <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        if not root:
            return 0

        d = compute_depth(root)
        if not d:
            return 1

        # 计算最后一层结点数
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if exists(root, d, pivot):
                left = pivot + 1
            else:
                right = pivot - 1

        return (2**d - 1) + left


# @lc code=end
