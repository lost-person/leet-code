#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        super().__init__()
        self.total = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        # morris 变形
        total = 0
        node = root
        while node:
            if node.right:
                succ = node.right
                while succ.left and succ.left != node:
                    succ = succ.left
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
            else:
                total += node.val
                node.val = total
                node = node.left

        return root

        # if root is not None:
        #     self.convertBST(root.right)
        #     self.total += root.val
        #     root.val = self.total
        #     self.convertBST(root.left)
        # return root

        # total = 0
        
        # node = root
        # stack = []
        # while stack or node:
        #     # push all nodes up to (and including) this subtree's maximum on
        #     # the stack.
        #     while node:
        #         stack.append(node)
        #         node = node.right

        #     node = stack.pop()
        #     total += node.val
        #     node.val = total

        #     # all nodes with values between the current and its parent lie in
        #     # the left subtree.
        #     node = node.left

        # return root

# @lc code=end

