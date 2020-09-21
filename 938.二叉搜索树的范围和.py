#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        if not root or L > R: return res
        
        node_list = [root]
        while node_list:
            node = node_list.pop()
            if L <= node.val <= R:
                res += node.val
            if node.left and node.val > L:
                node_list.append(node.left)
            if node.right and node.val < R:
                node_list.append(node.right)
        return res
# @lc code=end

