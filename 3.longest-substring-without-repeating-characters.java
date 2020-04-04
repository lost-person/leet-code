import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (26.63%)
 * Total Accepted:    761.5K
 * Total Submissions: 2.9M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string, find the length of the longest substring without repeating
 * characters.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "abcabcbb"
 * Output: 3 
 * Explanation: The answer is "abc", with the length of 3. 
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3. 
 * ⁠            Note that the answer must be a substring, "pwke" is a
 * subsequence and not a substring.
 * 
 * 
 * 
 * 
 * 
 */
class Solution {
    // // 动态规划求解(gg，超时了)
    // public int lengthOfLongestSubstring(String s) {
    //     // 长度
    //     int len = 0;
    //     for(int i = 0; i < s.length(); i++)
    //         for(int j = i + 1; j <= s.length(); j++)
    //             if(unique(s, i, j)) len = Math.max(len, j - i);
    //     return len;
    // }

    // public boolean unique(String s, int start, int end){
    //     Set<Character> set = new HashSet<>();
    //     Character c;
    //     for(int i = start; i < end; i++){
    //         c = s.charAt(i);
    //         if(set.contains(c)) return false;
    //         set.add(c);
    //     }
    //     return true;
    // }
    public int lengthOfLongestSubstring(String s) {
        int len = 0;
        // 存储当前元素的索引，从1开始
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0, j = 0; j < s.length(); j++){
            // 有重复元素
            if(map.containsKey(s.charAt(j)))
                i = Math.max(map.get(s.charAt(j)), i);
            len = Math.max(len, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return len;
    }
}
