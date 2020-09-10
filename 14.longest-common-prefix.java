/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (32.94%)
 * Total Accepted:    405.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * Note:
 * 
 * All given inputs are in lowercase letters a-z.
 * 
 */
class Solution {
    public static String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) return "";
        if(strs.length == 1) return strs[0];
        // 公共前缀子串肯定是所有字串的公共前缀子串，所以不如直接拿第一个
        int i = 0, j = 1;
        for(i = 0; i < strs[0].length(); i++){
            j = 1;
            while(j < strs.length){
                if(i == strs[j].length() || strs[0].charAt(i) != strs[j].charAt(i))
                    return strs[0].substring(0, i);
                j++;
            }
        }
        return strs[0];
    }
}
