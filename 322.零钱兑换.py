#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        
        if not amount:
            return 0

        # bfs
        coins.sort()
        queue = deque([amount])
        step = 0
        visited = set()

        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if tmp == 0:
                    return step
                for i in range(len(coins) - 1, -1, -1):
                    if tmp >= coins[i] and tmp - coins[i] not in visited:
                        visited.add(tmp - coins[i])
                        queue.appendleft(tmp - coins[i])
            step += 1
        return -1

        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0
        # for i in range(1, amount + 1):
        #     dp[i] = min(dp[i - c] if i - c >= 0 else float('inf') for c in coins) + 1
        
        # return dp[-1] if dp[-1] < float('inf') else -1
        
# @lc code=end

