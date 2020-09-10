#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        
        node_list = [root]
        while node_list:
            node = node_list.pop()
            res.append(node.val)

            if node.left:
                node_list.append(node.left)
            
            if node.right:
                node_list.append(node.right)
        
        return res[::-1]
# @lc code=end

