#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1: return 0

        prices = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

        left, right = 0, 0
        total_sum = 0
        res = 0
        index = 0
        
        for i, price in enumerate(prices):
            if price > 0: res += price
        
        return res
# @lc code=end

