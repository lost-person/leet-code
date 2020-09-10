#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 暴力 略
        if not T:
            return []
        
        n = len(T)
        res = [0] * n
        nxt = [float('inf')] * 102

        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_index < float('inf'):
                res[i] = warmer_index - i
            nxt[T[i]] = i
        return res
        
        # stack = []
        # for i in range(n - 1, -1, -1):
        #     while stack and T[i] >= T[stack[-1]]:
        #         stack.pop()
        #     if stack:
        #         res[i] = stack[-1] - i
        #     stack.append(i)
        # return res

# @lc code=end

