/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (26.44%)
 * Total Accepted:    470.9K
 * Total Submissions: 1.8M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, find the longest palindromic substring in s. You may
 * assume that the maximum length of s is 1000.
 * 
 * Example 1:
 * 
 * 
 * Input: "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "cbbd"
 * Output: "bb"
 * 
 * 
 */
class Solution {
    public String longestPalindrome(String s) {
    // 方法1 动态规划
    //    if(s.isEmpty()) return "";
    //    int n = s.length();
    //    // dp数组记录字符i到字符j的最长回文串长度
    //    int[][] dp = new int[n][n];
    //    // 记录最长回文子串长度
    //    int maxLen = 1;
    //    // 记录最长回文子串长度
    //    int start = 0;
    //    int i = 0;
    //    for(; i < n; i++){
    //        dp[i][i] = 1;
    //        if(i < n - 1){
    //            if(s.charAt(i) == s.charAt(i + 1)){
    //                dp[i][i+1] = 1;
    //                start = i;
    //                maxLen = 2;
    //            }
    //        }
    //    }
    //    int j = 0, k = 0;
    //    // i表示遍历长度
    //    for(i = 3; i <= n; i++){
    //        // j表示起始位置
    //        for(j = 0; j <= n - i; j++){
    //             k = i + j - 1;
    //             if(s.charAt(j) == s.charAt(k) && dp[j + 1][k - 1] == 1){
    //                 dp[j][k] = 1;
    //                 start = j;
    //                 maxLen = i;
    //             }
    //        }
    //    }
    //    return s.substring(start, start + maxLen);

        // 方法2（没想到）
        if(s.isEmpty()) return "";
        int n = s.length();
        int start = 0, end = 0;
        int i = 0;
        int len = 0, len1 = 0, len2 = 0;
        for(; i < n; i++){
            // 回文串两种情况，i表示回文串中心
            len1 = expandAroundCenter(s, i, i);
            len2 = expandAroundCenter(s, i, i + 1);
            len = Math.max(len1, len2);
            if(len > end - start){
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    public static int expandAroundCenter(String s, int left, int right){
        int l = left, r = right;
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }
        return r - l - 1;
    }
}
