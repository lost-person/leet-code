#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res = []
        node_list = [root]
        while node_list:
            m = len(node_list)
            tmp = []
            
            for i in range(m):
                tmp.append(node_list[i].val)
                if node_list[i].left: node_list.append(node_list[i].left)
                if node_list[i].right: node_list.append(node_list[i].right)

            res.insert(0, tmp)
            node_list = node_list[m:]
        
        return res
# @lc code=end

