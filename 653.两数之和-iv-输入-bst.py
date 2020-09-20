#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False

        node_list, s = [root], set()

        for node in node_list:
            v = node.val
            l = node.left
            r = node.right

            if k - v in s: return True
            s.add(v)

            if l: node_list.append(l)
            if r: node_list.append(r)
        return False


# @lc code=end
