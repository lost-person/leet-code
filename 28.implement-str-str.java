/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Implement strStr()
 *
 * https://leetcode.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (31.22%)
 * Total Accepted:    383.6K
 * Total Submissions: 1.2M
 * Testcase Example:  '"hello"\n"ll"'
 *
 * Implement strStr().
 * 
 * Return the index of the first occurrence of needle in haystack, or -1 if
 * needle is not part of haystack.
 * 
 * Example 1:
 * 
 * 
 * Input: haystack = "hello", needle = "ll"
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: haystack = "aaaaa", needle = "bba"
 * Output: -1
 * 
 * 
 * Clarification:
 * 
 * What should we return when needle is an empty string? This is a great
 * question to ask during an interview.
 * 
 * For the purpose of this problem, we will return 0 when needle is an empty
 * string. This is consistent to C's strstr() and Java's indexOf().
 * 
 */
class Solution {
    public int strStr(String haystack, String needle) {
        // // 方法1 逐个匹配
        // if(haystack.length() < needle.length()) return -1;
        // if(needle.length() == 0 || haystack.length() == 0) return 0;
        
        // int m = haystack.length();
        // int n = needle.length();
        // int i = 0, j = 0, index = 0;
        // for(; i <= m - n; i++){
        //     if(haystack.charAt(i) == needle.charAt(0)){
        //         index = i + 1; 
        //         j = 1;
        //         while(j < n && haystack.charAt(index) == needle.charAt(j)){
        //             index++;
        //             j++;
        //         }
        //         if(j == n) return i;
        //     }
        // }
        // return -1;

        // 方法2 KMP算法
        if(haystack.length() < needle.length()) return -1;
        if(needle.length() == 0 || haystack.length() == 0) return 0;

        int i = 0, j = 0;
        int m = haystack.length(), n = needle.length();
        int[] next = getNext(needle);
        while(i < m && j < n){
            // 匹配
            if(j == -1 || haystack.charAt(i) == needle.charAt(j)){
                i++;
                j++;
            }
            // 不匹配，重新调整
            else 
                j = next[j];
        }
        if(j == n) return i - j;
        else return -1;
    }

    // 获取KMP算法中的next数组
    public int[] getNext(String str){
        int n = str.length();
        int[] next = new int[n];

        next[0] = -1;

        int i = 0, j = -1;
        while(i < n - 1){
            // 匹配
            if(j == -1 || str.charAt(i) == str.charAt(j)){
                i++;
                j++;
                next[i] = j;
            }
            else
                j = next[j];
        }
        return next;
    }
}

