import java.util.Set;
import java.util.HashSet;

/*
 * @lc app=leetcode id=753 lang=java
 *
 * [753] Cracking the Safe
 *
 * https://leetcode.com/problems/cracking-the-safe/description/
 *
 * algorithms
 * Hard (44.66%)
 * Total Accepted:    12.3K
 * Total Submissions: 27.6K
 * Testcase Example:  '1\n1'
 *
 * 
 * There is a box protected by a password.  The password is n digits, where
 * each letter can be one of the first k digits 0, 1, ..., k-1.
 * 
 * You can keep inputting the password, the password will automatically be
 * matched against the last n digits entered.
 * 
 * For example, assuming the password is "345", I can open it when I type
 * "012345", but I enter a total of 6 digits.
 * 
 * Please return any string of minimum length that is guaranteed to open the
 * box after the entire string is inputted.
 * 
 * 
 * Example 1:
 * 
 * Input: n = 1, k = 2
 * Output: "01"
 * Note: "10" will be accepted too.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: n = 2, k = 2
 * Output: "00110"
 * Note: "01100", "10011", "11001" will be accepted too.
 * 
 * 
 * 
 * Note:
 * 
 * n will be in the range [1, 4].
 * k will be in the range [1, 10].
 * k^n will be at most 4096.
 * 
 * 
 */
class Solution {
    Set<String> seen = new HashSet<>();
    StringBuilder ans = new StringBuilder();
    public String crackSafe(int n, int k) {
        // 方法1 贪心
        if(n == 1 && k == 1) return "0";
        StringBuilder sb = new StringBuilder();
        int i = 0, j = 0;
        // 创建长度为n的全为0的密码
        for(; i < n; i++)
            sb.append("0");
        // 存储密码
        Set<String> set = new HashSet<>();
        set.add(sb.toString());
        String pre = "", cur = "";
        // 最多k^n种密码
        for(i = 0; i < Math.pow(k, n); i++){
            // 取最后n - 1个数
            pre = sb.substring(sb.length() - n + 1);
            // 每次从k-1递减
            for(j =  k - 1; j >= 0; j --){
               cur = pre + String.valueOf(j);
               if(!set.contains(cur)){
                   set.add(cur);
                   sb.append(String.valueOf(j));
                   break;
               }
            }
        }
        return sb.toString();
    }
    //     // 递归版本
    //     if (n == 1 && k == 1) return "0";
    //     StringBuilder sb = new StringBuilder();
    //     for (int i = 0; i < n-1; ++i)
    //         sb.append("0");
    //     String start = sb.toString();

    //     dfs(start, k);
    //     ans.append(start);
    //     return new String(ans);
    // }

    // public void dfs(String node, int k) {
    //     for (int x = 0; x < k; ++x) {
    //         String nei = node + x;
    //         if (!seen.contains(nei)) {
    //             seen.add(nei);
    //             dfs(nei.substring(1), k);
    //             ans.append(x);
    //         }
    //     }
    // }
}

