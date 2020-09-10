#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return head

        minHead = ListNode(-1)
        maxHead = ListNode(-1)

        dummy1, dummy2 = minHead, maxHead

        p = head
        while p:
            if p.val < x:
                minHead.next = p
                minHead = minHead.next
            else:
                maxHead.next = p
                maxHead = maxHead.next
            p = p.next
        maxHead.next = None
        minHead.next = dummy2.next
        return dummy1.next
# @lc code=end
