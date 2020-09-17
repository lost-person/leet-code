#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root: return res

        def path_sum(node, sum, tmp):
            if not node.left and not node.right and node.val == sum:
                res.append(tmp + [node.val])
                return

            tmp = tmp + [node.val]
            if node.left:
                path_sum(node.left, sum - node.val, tmp)
            if node.right:
                path_sum(node.right, sum - node.val, tmp)

        path_sum(root, sum, [])
        return res


# @lc code=end
