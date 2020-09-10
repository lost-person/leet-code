#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def dfs(node: TreeNode, prev_sum: int):
            if not node:
                return 0
            
            return int(node.val == prev_sum) + dfs(node.left, prev_sum - node.val) + dfs(node.right, prev_sum - node.val)

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
# @lc code=end

