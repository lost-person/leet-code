/*
 * @lc app=leetcode id=10 lang=java
 *
 * [10] Regular Expression Matching
 *
 * https://leetcode.com/problems/regular-expression-matching/description/
 *
 * algorithms
 * Hard (24.93%)
 * Total Accepted:    273.6K
 * Total Submissions: 1.1M
 * Testcase Example:  '"aa"\n"a"'
 *
 * Given an input string (s) and a pattern (p), implement regular expression
 * matching with support for '.' and '*'.
 * 
 * 
 * '.' Matches any single character.
 * '*' Matches zero or more of the preceding element.
 * 
 * 
 * The matching should cover the entire input string (not partial).
 * 
 * Note:
 * 
 * 
 * s could be empty and contains only lowercase letters a-z.
 * p could be empty and contains only lowercase letters a-z, and characters
 * like . or *.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input:
 * s = "aa"
 * p = "a"
 * Output: false
 * Explanation: "a" does not match the entire string "aa".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * s = "aa"
 * p = "a*"
 * Output: true
 * Explanation: '*' means zero or more of the precedeng element, 'a'.
 * Therefore, by repeating 'a' once, it becomes "aa".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input:
 * s = "ab"
 * p = ".*"
 * Output: true
 * Explanation: ".*" means "zero or more (*) of any character (.)".
 * 
 * 
 * Example 4:
 * 
 * 
 * Input:
 * s = "aab"
 * p = "c*a*b"
 * Output: true
 * Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
 * it matches "aab".
 * 
 * 
 * Example 5:
 * 
 * 
 * Input:
 * s = "mississippi"
 * p = "mis*is*p*."
 * Output: false
 * 
 * 
 */
class Solution {
    /**
     * 匹配请况：1. 若有'*'，假设在j + 1处，则
     *              1) *做0：字符i与字符j+2判断是否匹配；
     *              2) *做多个：字符i与字符j匹配，然后判断字符i+1与字符j；
     *          2. 其他，则
     *              判断字符i与字符j匹配，然后判断字符i+1与字符j+1；
     * 
     */
    public boolean isMatch(String s, String p) {
        // // 方法1：递归
        // // 无字符
        // if(p.isEmpty()) return s.isEmpty();

        // boolean firstMatch = (!s.isEmpty() && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'));
        
        // /**
        //  * 逐个匹配
        //  * 1. 匹配情况1
        //  * 2. 匹配情况2
        //  */
        // if(p.length() >= 2 && p.charAt(1) == '*')
        //     return (isMatch(s, p.substring(2)) || (firstMatch && isMatch(s.substring(1), p)));
        // else
        //     return (firstMatch && isMatch(s.substring(1), p.substring(1)));
        // 方法2：动态规划
        // dp[i][j]记录字符i与字符j的匹配情况
        boolean dp[][] = new boolean[s.length() + 1][p.length() + 1];
        // 初始化
        dp[s.length()][p.length()] = true;
        
        // 遍历
        boolean firstMatch = true;
        int i = 0, j = 0;
        for(i = s.length(); i >= 0; i--){
            for(j = p.length() - 1; j >= 0; j--){
                // 字符i与字符j匹配情况
                firstMatch = i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.');
                // 情况1中的两个情形
                if(j + 1 < p.length() && p.charAt(j + 1) == '*')
                    dp[i][j] = dp[i][j + 2] || (firstMatch && dp[i + 1][j]);
                // 情况2
                else
                    dp[i][j] = firstMatch && dp[i + 1][j + 1];
            }
        }
        return dp[0][0];
    }
}
