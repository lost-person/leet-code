import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.LinkedList;

/*
 * @lc app=leetcode id=30 lang=java
 *
 * [30] Substring with Concatenation of All Words
 *
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
 *
 * algorithms
 * Hard (23.14%)
 * Total Accepted:    123.1K
 * Total Submissions: 532.1K
 * Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
 *
 * You are given a string, s, and a list of words, words, that are all of the
 * same length. Find all starting indices of substring(s) in s that is a
 * concatenation of each word in words exactly once and without any intervening
 * characters.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * ⁠ s = "barfoothefoobarman",
 * ⁠ words = ["foo","bar"]
 * Output: [0,9]
 * Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
 * respectively.
 * The output order does not matter, returning [9,0] is fine too.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * ⁠ s = "wordgoodgoodgoodbestword",
 * ⁠ words = ["word","good","best","word"]
 * Output: []
 * 
 * 
 */
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        // 方法1，暴力破解
        // 方法2
        List<Integer> res = new LinkedList<>();
        if(s.length() == 0 || words.length == 0) return res;

        // map -> key: words中的单词，value：单词出现的次数
        Map<String, Integer> map = new HashMap<>();
        for(String word : words)
            map.put(word, map.getOrDefault(word, 0) + 1);
        
        // 窗口扫描
        int i = 0, j = 0;
        int m = s.length(), n = words.length, word_len = words[0].length();
        for(i = 0; i < m - n * word_len + 1; i++){
            // 用于扫描
            Map<String, Integer> tmpMap = new HashMap<>();
            for(j = 0; j < n; j++){
                // 截取长度为word_len的字符串
                String tmpString = s.substring(i + j * word_len, i + (j + 1) * word_len);
                // 不包含基础字符串
                if(!map.containsKey(tmpString)) break;
                tmpMap.put(tmpString, tmpMap.getOrDefault(tmpString, 0) + 1);
                // 包含重复字符串
                if(tmpMap.get(tmpString) > map.get(tmpString)) break;
            }
            // 匹配成功
            if(j == n) res.add(i);
        }
        return res;
    }
}

