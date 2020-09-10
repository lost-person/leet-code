# coding = utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if not root or root == p or root == q:
        #     return root
        
        # left_root = self.lowestCommonAncestor(root.left, p, q)
        # right_root = self.lowestCommonAncestor(root.right, p, q)

        # if not left_root:
        #     return right_root
        
        # if not right_root:
        #     return left_root
        
        # return root

        node_list = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = node_list.pop()
            if node.left:
                node_list.append(node.left)
                parent[node.left] = node

            if node.right:
                node_list.append(node.right)
                parent[node.right] = node
            
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q
