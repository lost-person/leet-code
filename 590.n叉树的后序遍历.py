#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 迭代
        # res = []
        # if not root: return res

        # node_list = [root]
        # while node_list:
        #     node = node_list.pop()
        #     if node:
        #         res.append(node.val)
        #     node_list.extend(node.children)
        
        # return res[::-1]
        
        # 递归
        res = []
        if not root: return []

        def postTraversal(node):
            if not node: return

            for child in node.children:
                postTraversal(child)
            res.append(node.val)
        postTraversal(root)
        return res

# @lc code=end

