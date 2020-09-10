/*
 * @lc app=leetcode id=23 lang=java
 *
 * [23] Merge k Sorted Lists
 *
 * https://leetcode.com/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (32.91%)
 * Total Accepted:    341.7K
 * Total Submissions: 1M
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * 
 * Example:
 * 
 * 
 * Input:
 * [
 * 1->4->5,
 * 1->3->4,
 * 2->6
 * ]
 * Output: 1->1->2->3->4->4->5->6
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
    // 分治法
    public ListNode mergeKLists(ListNode[] lists) {
        return divideAndConquer(lists, 0, lists.length - 1);
    }

    public ListNode divideAndConquer(ListNode[] lists, int start, int end){
        // 终止
        if(start > end)
            return null;
        else if(start + 1 == end)
            return merge(lists[start], lists[end]);
        else if(start == end)
            return lists[start];
    
        int mid = start + (end - start) / 2;
        // 分治
        ListNode l = divideAndConquer(lists, start, mid);
        ListNode r = divideAndConquer(lists, mid + 1, end);
        // 合并
        return merge(l, r);
    }

    public ListNode merge(ListNode l, ListNode r){
        ListNode head = new ListNode(0);
        ListNode l3 = head;
        // 合并两列表
        while(l != null && r != null){
            if(l.val < r.val){
                l3.next = l;
                l = l.next;
            }
            else{
                l3.next = r;
                r = r.next;
            }
            l3 = l3.next;
        }
        if(l == null)
            l3.next = r;
        else
            l3.next = l;
        return head.next;
    }
}

