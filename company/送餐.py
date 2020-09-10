# coding = utf-8

def dijstra(n, x, dist, matrix):
    for j in range(1, n + 1):
        dist[j] = matrix[x][j]

    visited = [False] * (n + 1)
    visited[x] = True

    while True:
        t = -1
        
        for i in range(1, n + 1):
            if dist[i] < float("inf") and not visited[i]:
                if t == -1 or dist[t] > dist[i]:
                    t = i
        
        if t == -1:
            break

        visited[t] = True
        for i in range(1, n + 1):
            dist[i] = min(dist[i], dist[t] + matrix[t][i])

    return dist

n, m, T = map(int, input().split())

matrix = [[float("inf")] * (n + 1) for i in range(n + 1)]
visited = [False] * (n + 1)
dist1, dist2 = [0] * (n + 1), [0] * (n + 1)
for _ in range(m):
    x, y, d = map(int, input().split())
    matrix[x][y] = d
dist1 = dijstra(n, n, dist1, matrix)
dist2 = dijstra(n, 1, dist2, matrix)
result = (dist1[1] + dist2[n]) * T if n > 1 and m > 1 else 0
print(result)