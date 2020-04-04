/*
 * @lc app=leetcode id=29 lang=java
 *
 * [29] Divide Two Integers
 *
 * https://leetcode.com/problems/divide-two-integers/description/
 *
 * algorithms
 * Medium (16.07%)
 * Total Accepted:    180.3K
 * Total Submissions: 1.1M
 * Testcase Example:  '10\n3'
 *
 * Given two integers dividend and divisor, divide two integers without using
 * multiplication, division and mod operator.
 * 
 * Return the quotient after dividing dividend by divisor.
 * 
 * The integer division should truncate toward zero.
 * 
 * Example 1:
 * 
 * 
 * Input: dividend = 10, divisor = 3
 * Output: 3
 * 
 * Example 2:
 * 
 * 
 * Input: dividend = 7, divisor = -3
 * Output: -2
 * 
 * Note:
 * 
 * 
 * Both dividend and divisor will be 32-bit signed integers.
 * The divisor will never be 0.
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
 * this problem, assume that your function returns 231 − 1 when the division
 * result overflows.
 * 
 * 
 */
class Solution {
    public int divide(int dividend, int divisor) {
        // 方法1 暴力破解，太low了
        // if(dividend == 0) return 0;
        // if(dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;

        // // 结果
        // int res = 0;
        // // 符号
        // int sign = (dividend > 0) ^ (divisor > 0) ? -1 : 1; 

        // // 全部转换为正数
        // long x = Math.abs((long)dividend);
        // long y = Math.abs((long)divisor);

        // while(y <= x){
        //     res++;
        //     x -= y;
        // }
        // return res * sign;

        // 方法2 位移
        if(dividend == 0) return 0;
        if(dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        int x = Math.abs(dividend), y = Math.abs(divisor), res = 0;
        int i = 31;
        for(; i >= 0; i--){
            if((x >>> i) - y >= 0){
                res += 1 << i;
                x -= y << i;
            }
        }
        return (dividend > 0) == (divisor > 0) ? res : -res;
    }
}

