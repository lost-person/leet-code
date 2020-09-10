#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def max_path_sum(node):
            if not node: return 0

            left_max_path_sum = max(max_path_sum(node.left), 0)
            right_max_path_sum = max(max_path_sum(node.right), 0)
            
            # 当前路径的最大路径和
            curr_path_sum = node.val + left_max_path_sum + right_max_path_sum
            self.max_sum = max(self.max_sum, curr_path_sum)

            return node.val + max(left_max_path_sum, right_max_path_sum)

        self.max_sum = float('-inf')
        max_path_sum(root)
        return self.max_sum

# @lc code=end

