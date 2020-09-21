#
# @lc app=leetcode.cn id=639 lang=python3
#
# [639] 解码方法 2
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        n = len(s)
        dp = [0] * (n + 1)
        mod_num = 10**9 + 7

        dp[0] = 1
        dp[1] = 9 if s[0] == "*" else (0 if s[0] == "0" else 1)
        
        i = 1
        while i < n:
            if s[i] == "*":
                # 单独解码
                dp[i + 1] = (9 * dp[i]) % mod_num
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % mod_num
                elif s[i - 1] == "2":
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % mod_num
                elif s[i - 1] == "*":
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % mod_num
            else:
                # 单独解码
                if s[i] != "0":
                    dp[i + 1] = dp[i]

                # 联合解码
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % mod_num
                elif s[i - 1] == "2" and s[i] <= "6":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % mod_num
                elif s[i - 1] == "*":
                    dp[i + 1] = (dp[i + 1] + (2 if s[i] <= "6" else 1) * dp[i - 1]) % mod_num

            i += 1
        return dp[n]
# @lc code=end

