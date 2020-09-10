/*
 * @lc app=leetcode id=6 lang=java
 *
 * [6] ZigZag Conversion
 *
 * https://leetcode.com/problems/zigzag-conversion/description/
 *
 * algorithms
 * Medium (30.51%)
 * Total Accepted:    283.8K
 * Total Submissions: 930.3K
 * Testcase Example:  '"PAYPALISHIRING"\n3'
 *
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 * of rows like this: (you may want to display this pattern in a fixed font for
 * better legibility)
 * 
 * 
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * 
 * 
 * And then read line by line: "PAHNAPLSIIGYIR"
 * 
 * Write the code that will take a string and make this conversion given a
 * number of rows:
 * 
 * 
 * string convert(string s, int numRows);
 * 
 * Example 1:
 * 
 * 
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * 
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 * 
 */
class Solution {
    public String convert(String s, int numRows) {
        // 自己写的太丑了，就不看了
        int n = s.length();
        if(n == 1 || numRows == 1) return s;
        StringBuilder sb = new StringBuilder();
        int len = 2 * numRows - 2;
        int i = 0, j = 0;
        // i表示第i行
        for(; i < numRows; i++){
            // j表示递增
            for(j = 0; i + j < n; j += len){
                // 每个第i行的首字符之后的第j个字符与字符i在同一行
                sb.append(s.charAt(i + j));
                // 除第一行与最后一行外，做其他处理
                if(i != 0 && i != numRows - 1 && j + len - i < n)
                    sb.append(s.charAt(j + len - i));
            }
        }
        return sb.toString();
    }
}
