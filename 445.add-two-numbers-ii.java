import java.util.Stack;

import com.sun.tools.javac.util.List;

/*
 * @lc app=leetcode id=445 lang=java
 *
 * [445] Add Two Numbers II
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
        if(l1 == null  || l2 == null) return null;

        // 栈保存数据
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();

        ListNode p = l1;
        // 入栈
        while(p != null){
            s1.push(p.val);
            p = p.next;
        }

        p = l2;

        while(p != null){
            s2.push(p.val);
            p = p.next;
        }

        // 求和结果
        ListNode res = new ListNode(-1);
        p = res;
        int sum = 0;
        while(!s1.empty() || !s2.empty()){
            sum /= 10;
            if(!s1.empty()) sum += s1.pop();
            if(!s2.empty()) sum += s2.pop();

            ListNode newNode = new ListNode(sum % 10);
            newNode.next = p.next;
            p.next = newNode;
        }

        if(sum / 10 == 1){
            ListNode newNode = new ListNode(1);
            newNode.next = p.next;
            p.next = newNode;
        }
        return res.next;
    }
}

