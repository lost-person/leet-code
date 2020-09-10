#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ''
        
        node_list = [root]
        while node_list:
            node = node_list.pop(0)
            if node:
                s += str(node.val)
                node_list.append(node.left)
                node_list.append(node.right)
            else:
                s += "n"
            s += " "
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == 'n': return None

        data_list = data.split()
        root = TreeNode(int(data_list[0]))
        node_list = [root]
        
        i = 1
        while node_list:
            node = node_list.pop(0)
            if not node: continue
            node.left = TreeNode(int(data_list[i])) if data_list[i] != 'n' else None
            node.right = TreeNode(int(data_list[i + 1])) if data_list[i + 1] != 'n' else None
            i += 2
            node_list.append(node.left)
            node_list.append(node.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

