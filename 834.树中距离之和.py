#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if not N: return []
        if not edges: return [0]

        res, size, dp = [0] * N, [0] * N, [0] * N
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[str(u)].append(v)
            graph[str(v)].append(u)

        def dfs1(u: int, f: int):
            size[u] = 1
            dp[u] = 0

            for v in graph.get(str(u)):
                if v == f: continue
                dfs1(v, u)
                dp[u] += dp[v] + size[v]
                size[u] += size[v]
        
        def dfs2(u: int, f: int):
            res[u] = dp[u]
            for v in graph.get(str(u)):
                if v == f: continue

                pu, pv, su, sv = dp[u], dp[v], size[u], size[v]
                dp[u] -= (dp[v] + size[v])
                size[u] -= size[v]
                dp[v] += (dp[u] + size[u])
                size[v] += size[u]

                dfs2(v, u)

                dp[u], dp[v], size[u], size[v] = pu, pv, su, sv

        dfs1(0, -1)
        dfs2(0, -1)

        return res
# @lc code=end

