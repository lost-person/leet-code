#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        if not head.next: return head

        # 拼接成环，并统计节点个数
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        return new_head
# @lc code=end

