#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
from collections import defaultdict, deque

class Node:
    def __init__(self):
        super().__init__()
        self.value = 0.0
        self.parent = None

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # floyd
        graph = defaultdict(lambda: defaultdict(lambda:-1.0))
        var_set = set()
        for i in equations: var_set.update(i)
        for i in var_set: graph[i][i] = 1.0
        for i, j in zip(equations, values):
            x, y = i
            graph[x][y] = j
            graph[y][x] = 1.0 / j
        
        # for k in var_set:
        #     for i in var_set:
        #         if graph[i][k] != -1.0:
        #             for j in var_set:
        #                 if graph[k][j] !=-1.0 and graph[i][j] == -1.0 : graph[i][j] = graph[i][k] * graph[k][j]
            
        # return [graph[x][y] for x, y in queries]
        
        res = []
        if not equations or not equations[0] or not values:
            return res

        def dfs(s, e, visited):
            if s == e: return 1
            visited.add(s)
            res = 1
            for nxt in graph[s]:
                if nxt not in visited:
                    res = graph[s][nxt] * dfs(nxt, e, visited)
                    if res > 0:
                        return res
            return -1

        for s, e in queries:
            if s not in var_set or e not in var_set:
                res.append(-1)
            else:
                res.append(dfs(s, e, set()))

        return res

        # graph = defaultdict(dict)
        # var_set = set()

        # for equation, value in zip(equations, values):
        #     x, y = equation[0], equation[1]
        #     var_set.update(equation)
        #     graph[x][y] = value
        #     graph[y][x] = 1 / value

        # def bfs(s, e):
        #     queue = deque([[s, 1.0]])
        #     visited = set([s])
        #     while queue:
        #         tmp, val = queue.pop()
        #         if tmp == e:
        #             return val
        #         for nxt in graph[tmp]:
        #             if nxt not in visited:
        #                 visited.add(nxt)
        #                 queue.appendleft([nxt, val * graph[tmp][nxt]])
        #     return -1
        # return [bfs(*q) if q[0] in var_set and q[1] in var_set else -1.0 for q in queries]
# @lc code=end

