#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) -> None:
        self.res = float("inf")
        self.pre = -1

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs(node.left)
            
            if self.pre != -1:
                self.res = min(self.res, node.val - self.pre)
            self.pre = node.val
            
            dfs(node.right)

        dfs(root)
        return self.res
# @lc code=end

