/*
 * @lc app=leetcode id=12 lang=java
 *
 * [12] Integer to Roman
 *
 * https://leetcode.com/problems/integer-to-roman/description/
 *
 * algorithms
 * Medium (49.64%)
 * Total Accepted:    201.7K
 * Total Submissions: 406.3K
 * Testcase Example:  '3'
 *
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D
 * and M.
 * 
 * 
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 * 
 * For example, two is written as II in Roman numeral, just two one's added
 * together. Twelve is written as, XII, which is simply X + II. The number
 * twenty seven is written as XXVII, which is XX + V + II.
 * 
 * Roman numerals are usually written largest to smallest from left to right.
 * However, the numeral for four is not IIII. Instead, the number four is
 * written as IV. Because the one is before the five we subtract it making
 * four. The same principle applies to the number nine, which is written as IX.
 * There are six instances where subtraction is used:
 * 
 * 
 * I can be placed before V (5) and X (10) to make 4 and 9. 
 * X can be placed before L (50) and C (100) to make 40 and 90. 
 * C can be placed before D (500) and M (1000) to make 400 and 900.
 * 
 * 
 * Given an integer, convert it to a roman numeral. Input is guaranteed to be
 * within the range from 1 to 3999.
 * 
 * Example 1:
 * 
 * 
 * Input: 3
 * Output: "III"
 * 
 * Example 2:
 * 
 * 
 * Input: 4
 * Output: "IV"
 * 
 * Example 3:
 * 
 * 
 * Input: 9
 * Output: "IX"
 * 
 * Example 4:
 * 
 * 
 * Input: 58
 * Output: "LVIII"
 * Explanation: L = 50, V = 5, III = 3.
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: 1994
 * Output: "MCMXCIV"
 * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 * 
 */
class Solution {
    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        // 转换为字符串
        char[] arr = Integer.toString(num).toCharArray();
        int n = arr.length;
        int i = 0;
        for(; i < n; i++){
            sb = romanNumber(n, arr[i], sb);
            n--;
        }
        return sb.toString();
    }

    public StringBuilder romanNumber(int n, int num, StringBuilder sb){
        /**
         * 三种罗马数字
         * c1: 1
         * c2: 5
         * c3: 10
         *  */ 
        num = num - 48;
        String s1 = "", s2 = "0", s3 = "0";
        // 数字范围是1-3999
        if(n == 4)
            s1 = "M";
        else if(n == 3){
            s1 = "C";
            s2 = "D";
            s3 = "M";
        }
        else if(n == 2){
            s1 = "X";
            s2 = "L";
            s3 = "C";
        }
        else{
            s1 = "I";
            s2 = "V";
            s3 = "X";
        }
        // 根据num确定如何添加字符
        if(num == 5)
            sb.append(s2);
        else if(num == 9){
            sb.append(s1);
            sb.append(s3);
        }
        else if(num == 4){
            sb.append(s1);
            sb.append(s2);
        }
        else if(6 <= num && num <= 8){
            sb.append(s2);
            num -= 5;
        }
        if(1 <= num && num <= 3){
            int i = 0;
            for(; i < num; i++)
                sb.append(s1);
        }   
        return sb;
    }
}
