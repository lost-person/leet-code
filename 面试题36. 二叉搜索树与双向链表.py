# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def change_ptr(root, node):
            if not root:
                return node
            
            node = change_ptr(root.left, node)
            node.right = root
            root.left = node
            node = root
            node = change_ptr(root.right, node)
            return node

        dummy = TreeNode(-1)
        tail = change_ptr(root, dummy)
        # 修改头结点的前驱指针，补充尾指针的后继指针
        head = dummy.right
        head.left = tail
        tail.right = head
        return head
