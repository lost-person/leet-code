#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
from collections import deque
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        
        if not coins:
            return 0
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

# @lc code=end

