#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k or not len(prices):
            return 0
        

        def max_profit_inf(prices):
            dp_i_0 = 0
            dp_i_1 = -prices[0]

            for i in range(len(prices)):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, tmp - prices[i])
        
            return dp_i_0
        
        n = len(prices)
        if k > (n >> 1):
            return max_profit_inf(prices) 
        
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for i in range(n):
            for j in range(k, 0, -1):
                if not i:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        
        return dp[n - 1][k][0]
# @lc code=end

