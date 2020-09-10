#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        super().__init__()
        self.cnt = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def get_cnt(self):
        return self.cnt

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def is_connect(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return

        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        self.cnt -= 1
    
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0

        n = len(M)
        visited = [False] * n
        cnt = 0

        uf = UnionFind(n)
        for i in range(n):
            for j in range(i):
                if M[i][j] == 1:
                    uf.union(i, j)
        
        return uf.get_cnt()

        # def dfs(row):
        #     for col in range(m):
        #         if M[row][col] == 1 and not visited[col]:
        #             visited[col] = True
        #             dfs(col)
        
        
        # for row in range(m):
        #     if not visited[row]:
        #         dfs(row)
        #         cnt += 1
        
        # return cnt
        # queue = []
        # for row in range(M):
        #     if not visited[row]:
        #         queue.append(row)
        #         while queue:
        #             s = queue.pop()
        #             visited[s] = True
        #             for col in range(M):
        #                 if M[row][col] == 1 and not visited[col]:
        #                     queue.append(col)
        #         cnt += 1
        # return cnt

# @lc code=end

