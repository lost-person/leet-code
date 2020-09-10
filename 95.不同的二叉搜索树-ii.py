#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generate_trees(start, end):
            if start > end: return [None,]

            res = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        tree = TreeNode(i)
                        tree.left = left_tree
                        tree.right = right_tree
                        res.append(tree)
            return res
        
        return generate_trees(1, n) if n else []
        
# @lc code=end

