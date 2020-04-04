import java.util.Stack;
import java.util.Map;
import java.util.HashMap;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (35.86%)
 * Total Accepted:    516.4K
 * Total Submissions: 1.4M
 * Testcase Example:  '"()"'
 *
 * Given a string containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * 
 * 
 * Note that an empty string is also considered valid.
 * 
 * Example 1:
 * 
 * 
 * Input: "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "(]"
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "([)]"
 * Output: false
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: "{[]}"
 * Output: true
 * 
 * 
 */
class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        // 利用栈
        Stack<Character> stack = new Stack<>();
        int i = 0;
        char c = 0, top = 0;
        // 遍历
        for(; i < s.length(); i++){
            c = s.charAt(i);
            // 无法匹配，继续压入
            if(map.containsKey(c)){
                // 抛出栈顶元素
                top = stack.isEmpty() ? '#' : stack.pop();
                // 不匹配
                if(map.get(c) != top)
                    return false;
            }     
            else
                stack.push(c);  
        }
        return stack.isEmpty();
    }
}

