#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 快慢指针
        def find_mid_node(head):
            prev = None
            slow_node = head
            fast_node = head
            
            while fast_node and fast_node.next:
                prev = slow_node
                slow_node = slow_node.next
                fast_node = fast_node.next.next
            
            # 通过此方式，断开左边的列表
            if prev:
                prev.next = None
            
            return slow_node

        def sortedlist_to_bst(head):
            if not head: return None

            mid = find_mid_node(head)
            root = TreeNode(mid.val)
            
            if head == mid: return root
            
            root.left = sortedlist_to_bst(head)
            root.right = sortedlist_to_bst(mid.next)
            return root
        
        return sortedlist_to_bst(head)


# @lc code=end

