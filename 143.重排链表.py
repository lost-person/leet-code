#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next: return

        # 找到链表中的中间节点
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 翻转链表
        p, right = slow.next, None
        slow.next = None

        while p:
            right, right.next, p = p, right, p.next
        
        # 插入
        left = head
        while left and right:
            left.next, right.next, left, right = right, left.next, left.next, right.next
# @lc code=end

