#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.res = []
        if not root: return self.res

        self.prev = float("inf")
        self.max_cnt = 0
        self.cnt = 0
        
        def update(cur):
            if cur == self.prev:
                self.cnt += 1
            else:
                self.prev = cur
                self.cnt = 1
            
            if self.cnt == self.max_cnt:
                self.res.append(cur)
            elif self.cnt > self.max_cnt:
                self.res = [cur]
                self.max_cnt = self.cnt

        # morris
        node = root
        while node:
            if node.left:
                prev = node.left
                while prev.right and prev.right != node:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = node
                    node = node.left
                else:
                    prev.right = None
                    update(node.val)
                    node = node.right

            else:
                update(node.val)
                node = node.right
        
        return self.res
# @lc code=end

