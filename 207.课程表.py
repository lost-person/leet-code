#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from typing import List


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites or not prerequisites[0]:
            return True

        # # 拓扑排序 bfs
        # in_degree = [0] * numCourses
        # adj_matrix = [[] for _ in range(numCourses)]

        # for cur, pre in prerequisites:
        #     in_degree[cur] += 1
        #     adj_matrix[pre].append(cur)

        # queue = []
        # for i in range(numCourses):
        #     if not in_degree[i]:
        #         queue.append(i)

        # while queue:
        #     pre = queue.pop()
        #     numCourses -= 1
        #     for cur in adj_matrix[pre]:
        #         in_degree[cur] -= 1
        #         if not in_degree[cur]:
        #             queue.append(cur)

        # return not bool(numCourses)

        flag = [0] * numCourses
        adj_matrix = [[] for _ in range(numCourses)]

        def dfs(i):
            if flag[i] == -1: return True  # 节点已经在别的拓扑排序中访问
            if flag[i] == 1: return False  # 节点已经当前的拓扑排序中访问
            flag[i] = 1
            for j in adj_matrix[i]:
                if not dfs(j):
                    return False
            flag[i] = -1
            return True

        for cur, pre in prerequisites:
            adj_matrix[pre].append(cur)

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# @lc code=end
