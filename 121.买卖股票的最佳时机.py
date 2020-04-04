#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1: return 0

        # prices = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

        # left, right = 0, 0
        # total_sum = 0
        # res = 0
        # index = 0
        
        # for i, price in enumerate(prices):
        #     total_sum += price
        #     if total_sum > res:
        #         res = total_sum
        #         left = index
        #         right = i
            
        #     if total_sum < 0:
        #         total_sum = 0
        #         index = i + 1
        
        # return res
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
# @lc code=end

