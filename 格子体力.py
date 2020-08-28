# coding = utf-8

# 矩阵每个格子为消耗的体力，求从矩阵最上方到最下方消耗的最少体力

class Node:
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

class MinHeap:
    def __init__(self):
        super().__init__() 
        self.data = [Node(0, 0, 0)] # dummpy node
        self.cnt = 0
    
    def size(self):
        return self.cnt
    
    def empty(self):
        return self.cnt == 0
    
    def insert(self, node):
        self.data.append(node)
        self.cnt += 1
        self.__swim(self.cnt)
    
    def extract_min(self):
        if self.empty():
            return None
        
        node = self.data[1]
        self.data[self.cnt], self.data[1] = self.data[1], self.data[self.cnt]
        self.data.pop()
        self.cnt -= 1
        if not self.empty():
            self.__sink(1)
        return node
    
    def __swim(self, index):
        node = self.data[index]
        while index > 1 and self.data[index >> 1].dist > node.dist:
            self.data[index] = self.data[index >> 1]
            index >>= 1
        self.data[index] = node


    def __sink(self, index):
        node = self.data[index]
        while index << 1 <= self.cnt:
            tmp_index = index << 1
            if tmp_index + 1 <= self.cnt and self.data[tmp_index + 1].dist < self.data[tmp_index].dist:
                tmp_index += 1
            if self.data[index].dist < self.data[tmp_index].dist:
                break
            self.data[index] = self.data[tmp_index]
            index = tmp_index
        self.data[index] = node

m, n = map(int, input().split())

matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))

dp = [[float('inf')] * n for _ in range(m)]

min_heap = MinHeap()
for i in range(n):
    dp[0][i] = matrix[0][i]
    min_heap.insert(Node(0, i, matrix[0][i]))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while not min_heap.empty():
    node = min_heap.extract_min()
    
    for direction in directions:
        new_x = node.x + direction[0]
        new_y = node.y + direction[1]

        if 0 <= new_x < m and 0 <= new_y < n and dp[new_x][new_y] > node.dist + matrix[new_x][new_y]:
            dp[new_x][new_y] = node.dist + matrix[new_x][new_y]
            min_heap.insert(Node(new_x, new_y, dp[new_x][new_y]))

print(min(dp[m-1]))
