# coding = utf-8

# 找出安全用户（没有同时借款和还款）

n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    row, col = map(int, input().split(','))
    matrix[row - 1][col - 1] = 1

safe_user_set = set()
for row in range(n):
    if not any(matrix[row]):
        safe_user_set.add(row)


def dfs(row, visited):
    if row in visited:
        return False

    if row in safe_user_set:
        return True

    visited.add(row)
    for col in range(n):
        if matrix[row][col] == 1 and not dfs(col, visited):
            return False

    safe_user_set.add(row)
    return True


for row in range(n):
    if row not in safe_user_set:
        dfs(row, set())

print(' '.join(map(lambda x: str(x + 1), list(safe_user_set))))
