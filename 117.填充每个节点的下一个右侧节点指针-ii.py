#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = deque([root])
        
        # Outer while loop which iterates over 
        # each level
        while Q:
            
            # Note the size of the queue
            size = len(Q)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]
                
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # Since the tree has now been modified, return the root node
        return root

        if not root:
            return root
        
        def processChild(childNode, prev, leftmost):
            if childNode:
                if prev:
                    prev.next = childNode
                else:    
                    leftmost = childNode
                prev = childNode 
            return prev, leftmost

        leftmost = root
        
        while leftmost:
            # prev 下一层的节点 curr 当前层的遍历节点
            prev, curr = None, leftmost
            # 更新 leftmost 为下一层的最左节点
            leftmost = None

            while curr:
                prev, leftmost = processChild(curr.left, prev, leftmost)
                prev, leftmost = processChild(curr.right, prev, leftmost)
                
                curr = curr.next       
        return root

# @lc code=end

