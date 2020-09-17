#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next: return head

        cnt = 1
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while cnt < m:
            p = p.next
            cnt += 1

        head = p.next
        while cnt < n:
            q = head.next
            head.next = q.next
            q.next = p.next
            p.next = q
            cnt += 1

        return dummy.next


# @lc code=end
