# coding = utf-8

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        head2 = None
        while head:
            tmp = head.next
            head.next = head2
            head2 = head
            head = tmp

        return head2