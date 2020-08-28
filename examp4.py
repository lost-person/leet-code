# coding = utf-8

n, m = list(map(int, input().split()))
a = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = list(map(int, input().split()))
    a[x][y] = 1


def dfs(a, i, visited):
    for j in range(n):
        if a[i][j] == 1 and not visited[j]:
            visited[j] = True
            for k in range(n):
                if k != i and a[j][k] == 1:
                    a[i][k] = 1


for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(a, i, visited)

res = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == a[j][i] == 1:
            res += 1

print(res)
