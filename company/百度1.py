# coding = utf-8

def solve():
    m, n = map(int, input().split())

    matrix = []
    for i in range(m):
        matrix.append(list(input()))

    if not matrix or not matrix[0]: return 0

    max_len, prev = 0, 0
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tmp = dp[j]
            if matrix[i - 1][j - 1] == 'M':
                dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                max_len = max(max_len, dp[j])
            else:
                dp[j] = 0
            prev = tmp
    return max_len * max_len

print(solve())
