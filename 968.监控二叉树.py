#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        if not root: return self.res

        dummy_head = TreeNode(0)
        dummy_head.left = root
        
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left + right == 0:
                return 1
            elif left == 1 or right == 1:
                self.res += 1
                return 2
            else:
                return 0

        dfs(dummy_head)
        return self.res

# @lc code=end

