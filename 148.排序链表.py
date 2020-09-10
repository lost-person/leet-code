#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并
        # if not head or not head.next: return head
        # slow, fast = head, head.next
        
        # # 找到中点
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # # 分割
        # mid = slow.next
        # slow.next = None

        # left, right = self.sortList(head), self.sortList(mid)
        
        # # 合并
        # h = res = ListNode(-1)
        # while left and right:
        #     if left.val < right.val:
        #         h.next = left
        #         left = left.next
        #     else:
        #         h.next = right
        #         right = right.next
        #     h = h.next
        
        # if left:
        #     h.next = left  
        # else:
        #     h.next = right
        
        # return res.next

        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while h and i:
                    h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while h and i: 
                    h, i = h.next, i - 1
                
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: 
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next
# @lc code=end

