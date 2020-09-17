# coding = utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 修改中序遍历定义：先右，中根，最后左
        if not root:
            return

        # node_list = []
        # cur = root
        # while cur or node_list:
        #     while cur:
        #         node_list.append(cur)
        #         cur = cur.right
        #     cur = node_list.pop()
        #     k -= 1
        #     if k == 0:
        #         return cur.val
        #     cur = cur.left
        cur = root
        while cur:
            if cur.right:
                prev = cur.right
                while prev.left and prev.left != cur:
                    prev = prev.left
                if not prev.left:
                    prev.left = cur
                    cur = cur.right
                else:
                    prev.left = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.left
            else:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.left
