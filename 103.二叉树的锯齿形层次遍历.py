#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        res = []
        node_list = [root]
        while node_list:
            tmp = [node.val for node in node_list if node]
            res.append(tmp)
            m = len(node_list)
            node_list = node_list[::-1]
            for i in range(m):
                if len(res) % 2 == 0:
                    if node_list[i].left:
                        node_list.append(node_list[i].left)
                    if node_list[i].right:
                        node_list.append(node_list[i].right)
                else:
                    if node_list[i].right:
                        node_list.append(node_list[i].right)
                    if node_list[i].left:
                        node_list.append(node_list[i].left)  
            node_list = node_list[m:]
        return res

        # results = []
        # def dfs(node, level):
        #     if level >= len(results):
        #         results.append(deque([node.val]))
        #     else:
        #         if level % 2 == 0:
        #             results[level].append(node.val)
        #         else:
        #             results[level].appendleft(node.val)

        #     for next_node in [node.left, node.right]:
        #         if next_node is not None:
        #             dfs(next_node, level+1)

        # # normal level order traversal with DFS
        # dfs(root, 0)

        # return results


# @lc code=end

