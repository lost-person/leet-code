#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 迭代
        # res = []
        # if not root: return []

        # node_list = deque()
        # node_list.appendleft(root)

        # while node_list:
        #     node = node_list.popleft()
        #     if node:
        #         res.append(node.val)
        #         node_list.extendleft(node.children[::-1])
        
        # return res

        # 递归
        res = []
        if not root: return []

        def preTraversal(node):
            if not node: return

            res.append(node.val)
            for child in node.children:
                preTraversal(child)
        preTraversal(root)
        return res
# @lc code=end

