#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # predecessor is a Morris predecessor. 
        # In the 'loop' cases it could be equal to the node itself predecessor == root.
        # pred is a 'true' predecessor, 
        # the previous node in the inorder traversal.
        x = y = predecessor = pred = None
        
        while root:
            # If there is a left child
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:       
                # Predecessor node is one step left 
                # and then right till you can.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
 
                # set link predecessor.right = root
                # and go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                # break link predecessor.right = root
                # link is broken : time to change subtree and go right
                else:
                    # check for the swapped nodes
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred 
                    pred = root
                    
                    predecessor.right = None
                    root = root.right
            # If there is no left child
            # then just go right.
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred 
                pred = root
                
                root = root.right
        
        x.val, y.val = y.val, x.val

        # morris 遍历(中序遍历)
        def morris(root):
            cur = root
            while cur:
                # 寻求当前节点的前驱节点
                if cur.left:
                    prev = cur.left
                    while prev.right and prev.right != cur:
                        prev = prev.right
                    
                    if not prev.right:
                        prev.right = cur
                        cur = cur.left

                    else:
                        prev.right = None
                        print(cur.val)
                        cur = cur.right

                else:
                    print(cur.val)
                    cur = cur.right

        # morris 遍历(前序遍历)
        def morris(root):
            cur = root
            while cur:
                # 寻求当前节点的前驱节点
                if cur.left:
                    prev = cur.left
                    while prev.right and prev.right != cur:
                        prev = prev.right
                    
                    if not prev.right:
                        print(cur.val)
                        prev.right = cur
                        cur = cur.left
                        continue
                    else:
                        prev.right = None
                        cur = cur.right

                else:
                    print(cur.val)
                    cur = cur.right
        
        # 后序遍历
        def morris(root):
            dummy = TreeNode(-1)
            dummy.left = root
            cur = dummy
            while cur:
                if cur.left:
                    prev = cur.left
                    while prev.right and prev.right != cur:
                        prev = prev.right
                    if not prev.right:
                        prev.right = cur
                        cur = cur.left
                    else:
                        print_reverse(cur.left, prev)
                        prev.right = None
                        cur = cur.right
                else:
                    cur = cur.right
        
        def print_reverse(left, prev):
            reverse(left, prev)

            p = prev
            while True:
                print(p.val)
                if p == left:
                    break
                p = p.right
            reverse(prev, left)
        
        def reverse(left, prev):
            if left == prev:
                return
            x, y = left, left.right
            while True:
                z = y.right
                y.right = x
                x = y
                y = z
                if x == prev:
                    break

# @lc code=end

