# coding = utf-8
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None

        pre_idx = 0
        def build_tree(left, right):
            nonlocal pre_idx
            if left == right:
                return None
            
            val = preorder[pre_idx]
            root = TreeNode(val)
            
            pre_idx += 1
            in_index = inorder.index(val)
            root.left = build_tree(left, in_index)
            root.right = build_tree(in_index + 1, right)
            
            # 构建子树
            return root
        
        return build_tree(0, len(preorder))

        