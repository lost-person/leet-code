import java.util.List;
import java.util.ArrayList;

/*
 * @lc app=leetcode id=22 lang=java
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (53.11%)
 * Total Accepted:    301.1K
 * Total Submissions: 566.9K
 * Testcase Example:  '3'
 *
 * 
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * 
 * For example, given n = 3, a solution set is:
 * 
 * 
 * [
 * ⁠ "((()))",
 * ⁠ "(()())",
 * ⁠ "(())()",
 * ⁠ "()(())",
 * ⁠ "()()()"
 * ]
 * 
 */
class Solution {
    public List<String> generateParenthesis(int n) {
        // // 方法1 递归 最终结果
        // List<String> list = new LinkedList<>();
        // // n = 0返回空字符串
        // if(n == 0)
        //     list.add("");
        // else{
        //     int i = 0;
        //     for(; i < n; i++){
        //         for(String left : generateParenthesis(i)){
        //             for(String right : generateParenthesis(n - i - 1))
        //                 list.add("(" + left + ")" + right);
        //         }
        //     }
        // }
        // return list;
        // 方法2 动态规划 python java写的有点烦
        // """
        // :type n: int
        // :rtype: List[str]
        // """
 
        // r = [[] for i in range(n+1)]
        // r[0] = [""]
 
        // for i in range(1, n+1):
        //     for j in range(i):
        //         r[i] += ['('+k+')'+l for k in r[j] for l in r[i-j-1]]
 
        // return r[n]
        List<List<String>> res = new ArrayList<>();
        List<String> tmpList = new ArrayList<>();
        tmpList.add("");
        res.add(tmpList);
        int i = 0, j = 0;
        // 遍历n 动态规划
        for(i = 1; i < n + 1; i++){
            tmpList = new ArrayList<>();
            // 之前的解
            for(j = 0; j < i; j++)        
                for(String left : res.get(j))
                    for(String right : res.get(i - j  - 1))
                        tmpList.add("(" + left + ")" + right);
            res.add(tmpList); 
        }
        return res.get(res.size() - 1);
    }
}

