import java.util.List;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;
/*
 * @lc app=leetcode id=17 lang=java
 *
 * [17] Letter Combinations of a Phone Number
 *
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (40.24%)
 * Total Accepted:    343.7K
 * Total Submissions: 854K
 * Testcase Example:  '"23"'
 *
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent.
 * 
 * A mapping of digit to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * 
 * 
 * Note:
 * 
 * Although the above answer is in lexicographical order, your answer could be
 * in any order you want.
 * 
 */
class Solution {
    public List<String> letterCombinations(String digits) {
        // 记录对应关系
        Map<Character, String> map = new HashMap<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        List<String> list = new LinkedList<>();
        if(digits.length() != 0)
            phone2letter(map, list, digits, "");
        return list;
    }

    public void phone2letter(Map<Character, String> map, List<String> list, String digits, String combineString){
        // 映射完毕
        if(digits.length() == 0) {
            list.add(combineString);
            return;
        }
        else{
            char c = digits.charAt(0);
            String letters = map.get(c);
            String letter = "";
            int i = 0;
            for(; i < letters.length(); i++){
                letter = letters.substring(i, i + 1);
                phone2letter(map, list, digits.substring(1), combineString + letter);
            }
        }
    }
}
