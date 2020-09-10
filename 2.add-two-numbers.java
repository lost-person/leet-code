/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (30.49%)
 * Total Accepted:    755.3K
 * Total Submissions: 2.5M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * Example:
 * 
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p = l1, q = l2;
        ListNode head = new ListNode(0);
        ListNode r = head;
        // 进位
        int carry = 0;
        // 列表中元素的值
        int x, y;
        // 求和
        int sum;
        while(p != null || q != null){
            // 取数
            x = (p == null) ? 0 : p.val;
            y = (q == null) ? 0 : q.val;
            // 相加
            sum = carry + x + y;
            // 获取进位
            carry = sum / 10;
            // 当前位置的数
            r.next = new ListNode(sum % 10);
            r = r.next;
            // 遍历下一个
            if(p != null) p = p.next;
            if(q != null) q = q.next;
        }
        // 最后仍有进位未处理
        if(carry != 0)
            r.next = new ListNode(carry);
        return head.next;
    }
}
