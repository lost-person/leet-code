# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def dfs(node: TreeNode, sum: int, tmp_res: List[int]) -> List[int]:
            if not node.left and not node.right and node.val == sum:
                res.append(tmp_res + [node.val])
                return
            
            tmp_res = tmp_res + [node.val]
            if node.left:
                dfs(node.left, sum - node.val, tmp_res)
            if node.right:
                dfs(node.right, sum - node.val, tmp_res)
            

        dfs(root, sum, [])
        return res