# coding = utf-8

# n个人，n座城市。目的地x，两座城市的距离不对称。求最短路径的最大值。

def dijstra(n, x, dist, matrix):
    for j in range(1, n + 1):
        dist[j] = matrix[x][j]
    
    visited = [False] * (n + 1)
    visited[x] = True
    while True:
        t = -1
        for i in range(1, n + 1):
            if dist[i] < float('inf') and not visited[i]:
                if t == -1 or dist[t] > dist[i]:
                    t = i

        if t == -1:
            break

        visited[t] = True
        for i in range(1, n + 1):
            dist[i] = min(dist[i], dist[t] + matrix[t][i])

    return dist

def solve():
    n, m, x = map(int, input().split())
    
    dist1, dist2 = [0] * (n + 1), [0] * (n + 1)
    visited = [False] * (n + 1)
    matrix1 = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    matrix2 = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(m):
        row, col, dist = map(int, input().split())
        matrix1[row][col] = min(matrix1[row][col], dist)
        matrix2[col][row] = min(matrix2[col][row], dist)
    
    dist1 = dijstra(n, x, dist1, matrix1)
    dist2 = dijstra(n, x, dist2, matrix2)
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, dist1[i] + dist2[i])
    
    print(ans)
    
solve()