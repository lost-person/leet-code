# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ''
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                s += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                s += 'n'
            s += ' '
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == 'n':
            return None
        
        tree_node_list = data.split(' ')
        root = TreeNode(int(tree_node_list[0]))
        node_list = deque()
        node_list.append(root)
        i = 1
        while node_list:
            node = node_list.popleft()
            if node:
                node.left = TreeNode(int(tree_node_list[i])) if tree_node_list[i] != 'n' else None
                node.right = TreeNode(int(tree_node_list[i + 1])) if tree_node_list[i + 1] != 'n' else None
                i += 2
                node_list.append(node.left)
                node_list.append(node.right)
        return root