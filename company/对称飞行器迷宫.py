# coding = utf-8

# 飞行器从 S 出发，上下左右移动，也可中心跳转（最多5次），判断到达目标地点的最少次数。

from collections import deque

n, m = map(int, input().split('  '))

matrix = []
for i in range(n):
    matrix.append(list(input()))

si, sj = 0, 0

is_found = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            si = i
            sj = j
            is_found = True
            break
    if is_found:
        break

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 上下左右

# bfs
queue = deque()
queue.appendleft((si, sj, 5, 0))

while queue:
    row, col, cnt, step = queue.pop()
    if matrix[row][col] == 'E':
        break
    matrix[row][col] = '#'
    if 0 <= row + 1 < n and matrix[row + 1][col] != '#':
        queue.appendleft((row + 1, col, cnt, step + 1))
    if 0 <= col - 1 < m and matrix[row][col - 1] != '#':
        queue.appendleft((row, col - 1, cnt, step + 1))
    if 0 <= row -1 < n and matrix[row - 1][col] != '#':
        queue.appendleft((row - 1, col, cnt, step + 1))
    if 0 <= col + 1 < m and matrix[row][col + 1] != '#':
        queue.appendleft((row, col + 1, cnt, step + 1))
    if matrix[n - 1 - row][m - 1 - col] != '#' and 0 <= cnt:
        queue.appendleft((n - 1 - row, m - 1 - col, cnt - 1, step + 1))

print(step)
