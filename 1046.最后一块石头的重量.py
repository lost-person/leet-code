#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones or len(stones) == 0: return 0
        
        n = len(stones)
        if n == 1: return stones[0]

        stones_hp = []
        for stone in stones:
            heapq.heappush(stones_hp, -stone)
        
        while len(stones_hp) > 1 and stones_hp[0] < 0:
            heapq.heappush(stones_hp, heapq.heappop(stones_hp) - heapq.heappop(stones_hp))
        
        return -stones_hp[0]
# @lc code=end

