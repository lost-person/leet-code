#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root

        while node:
            if node.val < val:
                if not node.right:
                    new_node = TreeNode(val)
                    node.right = new_node
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    new_node = TreeNode(val)
                    node.left = new_node
                    break
                else:
                    node = node.left
        return root if root else TreeNode(val)


# @lc code=end
