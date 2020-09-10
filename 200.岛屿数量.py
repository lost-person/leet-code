#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def get_count(self):
        return self.count

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1
        self.count -= 1

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        m = len(grid)
        n = len(grid[0])

        # 岛屿数量
        cnt = 0

        def get_index(x, y):
            return x * n + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = m * n

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)
        for i in range(m):
            for j in range(n):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < m and new_y < n and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1

        # def dfs(i, j):
        #     if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] == '0':
        #         return
            
        #     grid[i][j] = '0'
        #     dfs(i - 1, j)
        #     dfs(i + 1, j)
        #     dfs(i, j - 1)
        #     dfs(i, j + 1)
        
        # for i in range(0, m):
        #     for j in range(0, n):
        #         if grid[i][j] == '1':
        #             cnt += 1
        #             dfs(i, j)
        # return cnt

        # bfs
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '0':
        #             continue

        #         cnt += 1
        #         grid[i][j] = '0'
        #         tmp_list = []
        #         tmp_list.append((i, j))
        #         while tmp_list:
        #             row, col = tmp_list.pop()
        #             if (row - 1) >= 0 and grid[row - 1][col] == '1':
        #                 tmp_list.append((row - 1, col))
        #                 grid[row - 1][col] = '0'
        #             if (row + 1) < m and grid[row + 1][col] == '1':
        #                 tmp_list.append((row + 1, col))
        #                 grid[row + 1][col] = '0'
        #             if (col - 1) >= 0 and grid[row][col - 1] == '1':
        #                 tmp_list.append((row, col - 1))
        #                 grid[row][col - 1] = '0'
        #             if (col + 1) < n and grid[row][col + 1] == '1':
        #                 tmp_list.append((row, col + 1))
        #                 grid[row][col + 1] = '0'
        
        # return cnt
# @lc code=end

