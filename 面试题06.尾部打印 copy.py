# coding = utf-8
class Solution:
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype
        """

        head2 = None
        while head:
            head, head2, head2.next = head.next, head, head2
        
        res = []
        while head2:
            res.append(head2.val)
            head2 = head2.next
        return res