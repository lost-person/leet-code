#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))

        prev = dummy # 用于寻找插入位置
        tail = dummy # 有序链表的尾部
        cur = head # 当前位置

        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                tmp = cur.next
                tail.next = tmp
                # 从头遍历寻找插入位置
                while prev.next and prev.next.val < cur.val:
                    prev = prev.next
                cur.next = prev.next
                prev.next = cur
                # 恢复
                prev = dummy
                cur = tmp
        
        return dummy.next
# @lc code=end

