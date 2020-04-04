#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        d_i_0 = 0
        d_i_1 = float('-inf')

        for price in prices:
            tmp = d_i_0
            d_i_0 = max(d_i_0, d_i_1 + price)
            d_i_1 = max(d_i_1, tmp - price - fee)
        return d_i_0
# @lc code=end

