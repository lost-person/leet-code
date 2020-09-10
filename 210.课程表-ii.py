#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        if not numCourses:
            return res
        
        # in_degree = [0] * numCourses
        # adj_matrix = [[] for _ in range(numCourses)]

        # for cur, pre in prerequisites:
        #     in_degree[cur] += 1
        #     adj_matrix[pre].append(cur)
        
        # queue = deque([cur for cur in range(numCourses) if in_degree[cur] == 0])

        # while queue:
        #     pre = queue.pop()
        #     res.append(pre)
        #     for cur in adj_matrix[pre]:
        #         in_degree[cur] -= 1
        #         if in_degree[cur] == 0:
        #             queue.append(cur)

        # return res if len(res) == numCourses else []

        # 0 未搜索，1 搜索中，2 搜索完成
        visited = [0] * numCourses
        adj_matrix = [[] for _ in range(numCourses)]
        for pre, cur in prerequisites:
            adj_matrix[pre].append(cur)

        is_cycle = False
        def dfs(pre: int):
            nonlocal is_cycle
            
            visited[pre] = 1
            for cur in adj_matrix[pre]:
                if not visited[cur]:
                    dfs(cur)
                    if is_cycle:
                        return
                elif visited[cur] == 1:
                    is_cycle = True
                    return

            visited[pre] = 2
            res.append(pre)
            return
        
        for pre in range(numCourses):
            if is_cycle:
                break

            if not visited[pre]:
                dfs(pre)

        return res if len(res) == numCourses else []
# @lc code=end

