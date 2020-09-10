#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 深度优先搜索
        # if not root: return 0

        # children = [root.left, root.right]
        
        # if not any(children):
        #     return 1
        
        # min_depth = float('inf')
        # for child in children:
        #     if child:
        #         min_depth = min(self.minDepth(child), min_depth)
        
        # return min_depth + 1

        # 深度优先搜索 栈实现
        # if not root:
        #     return 0
        # else:
        #     stack, min_depth = [(1, root),], float('inf')
        
        # while stack:
        #     depth, root = stack.pop()
        #     children = [root.left, root.right]
        #     if not any(children):
        #         min_depth = min(depth, min_depth)
        #     for c in children:
        #         if c:
        #             stack.append((depth + 1, c))
        
        # return min_depth 

        # 宽度优先搜索
        # if not root: return 0
        
        # node_deque = collections.deque([(1, root),])
        
        # while node_deque:
        #     depth, root = node_deque.popleft()
        #     children = [root.left, root.right]
        #     if not any(children):
        #         return depth
        #     for c in children:
        #         if c:
        #             node_deque.append((depth + 1, c))
        if root:
            if root.left and root.right:
                return 1+min(self.minDepth(root.left),self.minDepth(root.right))
            elif root.left:
                return 1+self.minDepth(root.left)
            elif root.right:
                return 1+self.minDepth(root.right)
            else:
                return 1
        else:
            return 0

# @lc code=end

