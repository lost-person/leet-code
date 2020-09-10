#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        ha = headA
        hb = headB

        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
# @lc code=end

