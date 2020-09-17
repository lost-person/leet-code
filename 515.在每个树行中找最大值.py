#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        node_list = [root]
        while node_list:
            n = len(node_list)
            tmp_num = float('-inf')
            for i in range(n):
                tmp_num = max(node_list[i].val, tmp_num)
                if node_list[i].left:
                    node_list.append(node_list[i].left)
                if node_list[i].right:
                    node_list.append(node_list[i].right)
            res.append(tmp_num)
            node_list = node_list[n:]
        return res


# @lc code=end
