#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        def sortedarray_to_bst(left, right):
            if left > right: return None

            mid = left + ((right - left) >> 1)

            val = nums[mid]
            root = TreeNode(val)

            root.left = sortedarray_to_bst(left, mid - 1)
            root.right = sortedarray_to_bst(mid + 1, right)

            return root

        return sortedarray_to_bst(0, len(nums) - 1)


# @lc code=end
