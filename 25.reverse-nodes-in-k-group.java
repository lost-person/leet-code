/*
 * @lc app=leetcode id=25 lang=java
 *
 * [25] Reverse Nodes in k-Group
 *
 * https://leetcode.com/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (35.29%)
 * Total Accepted:    168.2K
 * Total Submissions: 476.3K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given a linked list, reverse the nodes of a linked list k at a time and
 * return its modified list.
 * 
 * k is a positive integer and is less than or equal to the length of the
 * linked list. If the number of nodes is not a multiple of k then left-out
 * nodes in the end should remain as it is.
 * 
 * 
 * 
 * 
 * Example:
 * 
 * Given this linked list: 1->2->3->4->5
 * 
 * For k = 2, you should return: 2->1->4->3->5
 * 
 * For k = 3, you should return: 3->2->1->4->5
 * 
 * Note:
 * 
 * 
 * Only constant extra memory is allowed.
 * You may not alter the values in the list's nodes, only nodes itself may be
 * changed.
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
    // 没写出来，二刷
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head == null || k <= 1) return head;
        ListNode p = head;
        
        ListNode ans = new ListNode(0);
        ListNode nl = ans;
        while(p != null){
            int cnt = 0;
            ListNode newHead = null;    
            while(cnt < k && p != null){
                ListNode tmpn = p.next;  //翻转链表 必存节点
                p.next = newHead;
                newHead = p; // 翻转链表了 当cnt == k的时候就翻转成功了
                p = tmpn;  //移动 k次之后 是需要翻转的下一个结点
                cnt++;
            }
            // k个结点倒置，与之前结果相连
            if (cnt == k){
                nl.next = newHead;
                while(nl.next != null){
                    nl = nl.next;  // 最终又回到这个点
                }
            }
            // 剩余结点不足k个
            else{
                // 记录的时候已经改变了位置 所以直接翻转newHead结果就好了
                ListNode nn = null;  //新头节点
                while(newHead != null){
                    ListNode tt = newHead.next;
                    newHead.next = nn;
                    nn = newHead;
                    newHead = tt;  // 不断下移翻转
                }
                nl.next = nn;
            }
        }
        return ans.next;   
    }
}

