#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        def getIntersect(head):
            tortoise = head
            hare = head

            while hare is not None and hare.next is not None:
                tortoise = tortoise.next
                hare = hare.next.next
                if tortoise == hare:
                    return tortoise

            return None

        intersect = getIntersect(head)
        if intersect is None:
            return None

        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1


# @lc code=end
