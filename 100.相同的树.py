#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_same_tree(p_i, q_i):
            # p_i 节点为空时，判断 q_i 是否也为空
            if not p_i:
                return not q_i

            if not q_i:
                return not p_i

            if p_i.val != q_i.val:
                return False
            if not (is_same_tree(p_i.left, q_i.left)
                    and is_same_tree(p_i.right, q_i.right)):
                return False

            return True

        return is_same_tree(p, q)


# @lc code=end
