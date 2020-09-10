/*
 * @lc app=leetcode id=24 lang=java
 *
 * [24] Swap Nodes in Pairs
 *
 * https://leetcode.com/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (43.11%)
 * Total Accepted:    281.6K
 * Total Submissions: 652.7K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given a linked list, swap every two adjacent nodes and return its head.
 * 
 * You may not modify the values in the list's nodes, only nodes itself may be
 * changed.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        // 虚拟头节点
        dummy.next = head;
        ListNode cur = dummy;
        while(cur.next != null && cur.next.next != null){
            ListNode fir = cur.next;
            ListNode sec = fir.next;
            cur.next = sec;
            fir.next = sec.next;
            sec.next = fir;
            cur = cur.next.next;
        }
        return dummy.next;
    }
}

