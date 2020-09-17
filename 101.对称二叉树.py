#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        # self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归
        # if not root: return True

        # def is_symmetric(left_node, right_node):
        #     if not left_node and not right_node: return True
        #     if not left_node or not right_node: return False

        #     return left_node.val == right_node.val and is_symmetric(left_node.left, right_node.right) and \
        #             is_symmetric(left_node.right, right_node.left)

        # return is_symmetric(root.left, root.right)

        if not root: return True
        res = [root.left, root.right]

        while res:
            node1 = res.pop()
            node2 = res.pop()
            if not node1 and not node2: continue
            if not node1 or not node2: return False
            if node1.val != node2.val: return False
            res.append(node1.left)
            res.append(node2.right)
            res.append(node1.right)
            res.append(node2.left)
        return True


# @lc code=end
