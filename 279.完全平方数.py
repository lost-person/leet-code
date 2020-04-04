#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4: return n

        def isSquare(n: int) -> bool:
            sq = int(math.sqrt(n))
            return sq*sq == n
        
        if isSquare(n): return 1
        candidates = {i ** 2 for i in range(1, int(n ** 0.5 + 1))}
        queue = deque([n])
        step = 0
        while queue:
            step += 1
            m = len(queue)
            for _ in range(m):
                tmp = queue.pop()
                for x in candidates:
                    val = tmp - x
                    if val in candidates:
                        return step + 1
                    elif val > 0:
                        queue.appendleft(val)

        # 动态规划
        # dp = list(range(n + 1))
        # for i in range(4, n + 1):
        #     for j in range(1, int(i ** 0.5) + 1):
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)
        # return dp[n]

        # dp = [0]
        # while len(dp) <= n:
        #     dp.append(min(dp[- i ** 2] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1)
        # return dp[n]

        # Lagrange's four-square theorem (https://blog.csdn.net/l_mark/article/details/89044137)
        # if isSquare(n):
        #     return 1
        # # n 是4 的整倍数
        # while (n & 3) == 0:
        #     n >>= 2
        # if (n & 7) == 7:
        #     return 4
        # sq = int(math.sqrt(n)) + 1
        # for i in range(1, sq):
        #     if isSquare(n - i*i):
        #         return 2
        # return 3



# @lc code=end

