#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        # 回溯递归
        coordinate = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        def code(row, col):
            """位编码，太强了
            """
            return 1 << (row * n + col)
        
        def neightbors(row, col):
            """有效的邻居节点
            """
            for i in range(4):
                new_row = row + coordinate[i][0]
                new_col = col + coordinate[i][1]
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] % 2 == 0:
                    yield new_row, new_col
        
        target = 0
        sr, sc = -1, -1
        tr, tc = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] % 2 == 0:
                    target |= code(i, j)
                if grid[i][j] == 1:
                    sr, sc = i, j
                elif grid[i][j] == 2:
                    tr, tc = i, j
        
        def dp(row, col, todo):
            if row == tr and col == tc:
                return +(todo == 0)
            
            ans = 0
            for nr, nc in neightbors(row, col):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            
            return ans
        
        return dp(sr, sc, target)

        # todo = 0
        # sr, sc = 0, 0
        # tr, tc = 0, 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] != -1:
        #             todo += 1
        #         if grid[i][j] == 1:
        #             sr, sc = i, j
        #         elif grid[i][j] == 2:
        #             tr, tc = i, j

        # self.res = 0

        # self.res = 0

        # def dfs(row, col, todo):
        #     todo -= 1
        #     if todo < 0:
        #         return
            
        #     if row == tr and col == tc:
        #         if not todo:
        #             self.res += 1
        #             return 
            
        #     grid[row][col] = 3
        #     for i in range(4):
        #         new_row = row + coordinate[i][0]
        #         new_col = col + coordinate[i][1]
        #         if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] % 2 == 0:
        #             dfs(new_row, new_col, todo)
            
        #     grid[row][col] = 0

        # dfs(sr, sc, todo)
        # return self.res
# @lc code=end

