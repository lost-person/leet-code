#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        
        def bfs(root: TreeNode):
            if not root:
                return
            
            queue = [root]
            while queue:
                res.append(queue[-1].val)
                nxt = []
                for node in queue:
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                queue = nxt

            return
        bfs(root)
        return res

        # def dfs(root, depth):
        #     if not root:
        #         return 
        #     if len(res) <= depth:
        #         res.append(0)
        #     res[depth] = root.val
        #     dfs(root.left, depth + 1)
        #     dfs(root.right, depth + 1)
        
        # dfs(root, 0)
        # return res
# @lc code=end

