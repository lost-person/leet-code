/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 *
 * https://leetcode.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (41.76%)
 * Total Accepted:    504.7K
 * Total Submissions: 1.2M
 * Testcase Example:  '121'
 *
 * Determine whether an integer is a palindrome. An integer is a palindrome
 * when it reads the same backward as forward.
 * 
 * Example 1:
 * 
 * 
 * Input: 121
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it
 * becomes 121-. Therefore it is not a palindrome.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a
 * palindrome.
 * 
 * 
 * Follow up:
 * 
 * Coud you solve it without converting the integer to a string?
 * 
 */
class Solution {
    public boolean isPalindrome(int x) {
        // // 方法1：转换为字符串
        // if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        // if(x == 0) return true;
        // int num = x;
        // // 将整数转换为字符串
        // StringBuilder sb = new StringBuilder();
        // while(num > 0){
        //     sb.append(num % 10);
        //     num = num / 10;
        // }
        // String s = sb.toString();
        // // 判断是否为回文串
        // int start = 0, end = s.length() - 1;
        // while(start <= end){
        //     if(s.charAt(start) != s.charAt(end))
        //         return false;
        //     start++;
        //     end--;
        // }
        // return true;
        // // 方法2：转换为字符串
        // if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        // char[] arr = Integer.toString(x).toCharArray();
        // int start = 0, end = arr.length - 1;
        // while (start <= end) {
        //     if(arr[start] != arr[end])
        //         return false;
        //     start++;
        //     end--;
        // }
        // return true;
        // 方法3: 直接判断
        if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        int num = x;
        int mod = 0, rev = 0;
        while(num > 0){
            mod = num % 10;
            num = num /10;
            rev = rev * 10 + mod; 
        }
        return rev == x? true: false;
    }
}
