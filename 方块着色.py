# coding = utf-8

# 从矩阵最上方到最下方，但是不能上下移动

n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

dp = matrix[0]

for i in range(1, n):
    tmp_dp = dp[:]
    for j in range(m):
        dp[j] = matrix[i][j] + min(tmp_dp[:j] + tmp_dp[j + 1:])

print(min(dp))
