# coding = utf-8

# 给定一个数组n，然后给三个长度为n的数组，可以从这三个数组中选出一个长度为n的数组，
# 第i个位置需要是从给出的三个数组第i个位置选择的，然后要求使这个数组后一项减前一项的绝对值之和最小。


def solve():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    dp = [0] * 3
    tmp = [0] * 3
    for i in range(n):
        for j in range(3):
            tmp[j] = min(
                abs(matrix[j][i] - matrix[0][i - 1]) + dp[0],
                abs(matrix[j][i] - matrix[1][i - 1]) + dp[1],
                abs(matrix[j][i] - matrix[2][i - 1]) + dp[2])
        dp = tmp[:]

    return min(dp)


print(solve())
