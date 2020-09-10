#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        # # 记忆化回溯
        # memo = [[-1] * n for _ in range(n)]

        # def can_Cross(idx: int, jump_size: int):
        #     if memo[idx][jump_size] >= 0:
        #         return memo[idx][jump_size]
            
        #     for i in range(idx + 1, n):
        #         gap = stones[i] - stones[idx]
        #         if jump_size - 1 <= gap <= jump_size + 1:
        #             if can_Cross(i, gap) == 1:
        #                 memo[idx][gap] = 1
        #                 return 1
        #     memo[idx][jump_size] = 1 if idx == n - 1 else 0
        
        #     return memo[idx][jump_size]
        
        # return can_Cross(0, 0) == 1

        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True
        for i in range(1, n):
            for j in range(i):
                gap = stones[i] - stones[j]
                if gap < 0 or gap >= n or not dp[j][gap]:
                    continue
                dp[i][gap] = True
                if gap - 1 >= 0:
                    dp[i][gap - 1] = True
                if gap + 1 < n:
                    dp[i][gap + 1] = True
        
        return any(dp[-1])
# @lc code=end

