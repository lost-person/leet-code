import java.util.Stack;

/*
 * @lc app=leetcode id=32 lang=java
 *
 * [32] Longest Valid Parentheses
 *
 * https://leetcode.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (24.91%)
 * Total Accepted:    173.4K
 * Total Submissions: 695.9K
 * Testcase Example:  '"(()"'
 *
 * Given a string containing just the characters '(' and ')', find the length
 * of the longest valid (well-formed) parentheses substring.
 * 
 * Example 1:
 * 
 * 
 * Input: "(()"
 * Output: 2
 * Explanation: The longest valid parentheses substring is "()"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ")()())"
 * Output: 4
 * Explanation: The longest valid parentheses substring is "()()"
 * 
 * 
 */
class Solution {
    public int longestValidParentheses(String s) {
        // // 方法1 匹配长度
        // // 最长匹配长度
        // int len = 0;
        // int n = s.length();
        // if(s.length() <= 1) return len;

        // int i = 1;
        // int[] dp = new int[n];
        // for(; i < n; i++){
        //     // 可能匹配
        //     if(s.charAt(i) == ')'){
        //         // 相邻匹配
        //         if(s.charAt(i - 1) == '(') dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
        //         // 非相邻匹配
        //         else if(i - dp[i - 1] > 0 && s.charAt(i - dp[i - 1] - 1) == '(')
        //             dp[i] = dp[i - 1] + ((i - dp[i - 1] >= 2) ? dp[i - dp[i - 1] - 2] : 0) + 2;
        //         // 更新
        //         len = Math.max(len, dp[i]);
        //     }
        // }
        // return len;

        // 方法2 栈
        int len = 0;
        int n = s.length();
        if(s.length() <= 1) return len;

        Stack<Integer> stack = new Stack<>();
        // 初始化，方便操作
        stack.push(-1);
        int i = 0;
        for(; i < n; i++){
            // 无法匹配
            if(s.charAt(i) == '(') stack.push(i);
            else{
                stack.pop();
                // 可能第一个字符是')'
                if(stack.empty()) stack.push(i);
                else len = Math.max(len, i - stack.peek());
            }
        }
        return len;
    }
}

