#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 左端点
        events = sorted([(L, -H, R) for L, R, H in buildings] +
                        list({(R, 0, 0)
                              for _, R, _ in buildings}))
        res = [[0, 0]]
        heap = [[0, float("inf")]]
        for x, H, R in events:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if H:
                heapq.heappush(heap, [H, R])
            # 转折点
            if res[-1][1] != -heap[0][0]:
                res.append([x, -heap[0][0]])
        return res[1:]


# @lc code=end
