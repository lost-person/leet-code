#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        slow = dummy.next
        fast = dummy.next.next

        while fast:
            # 重复一直遍历直至不重复的元素
            if fast.val == slow.val:
                fast = fast.next
            else:
                if slow.next == fast:
                    prev = prev.next
                    slow = slow.next
                    fast = fast.next
                else:
                    slow = fast
                    prev.next = slow
                    fast = fast.next
        if slow.next:
            prev.next = None
        return dummy.next


# @lc code=end
