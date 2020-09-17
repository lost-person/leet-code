#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0]: return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                res[i:][0] = [0] * (m - i)
                break
            else:
                res[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                res[0][j:] = [0] * (n - j)
                break
            else:
                res[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]


# @lc code=end
