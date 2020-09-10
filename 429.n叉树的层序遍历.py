#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 迭代
        # res = []
        # if not root: return res

        # node_list = [root]

        # while node_list:
        #     n = len(node_list)
        #     res.append([])
        #     for i in range(n):
        #         if node_list[i]:
        #             res[-1].append(node_list[i].val)
        #             node_list.extend(node_list[i].children)
        #     node_list = node_list[n:]
        # return res

        # 递归
        res = []
        if not root: return res

        def traverse_node(node, level):
            if len(res) == level:
                res.append([])

            res[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        traverse_node(root, 0)
        return res            
# @lc code=end

