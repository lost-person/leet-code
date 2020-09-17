# coding = utf-8

# 对一个数字串，等概率取任意一段连续子串，求取出的子串的最大值的期望。


def solve():
    n = int(input())
    value_list = list(map(int, input().split()))
    stack = [(value_list[0], 0)]
    dp = [0] * n
    res = value_list[0]

    for i in range(1, n):
        while stack and value_list[i] >= stack[-1][0]:
            stack.pop()

        if not stack:
            dp[i] = (i + 1) * value_list[i]
        else:
            dp[i] = (i - stack[-1][1]) * value_list[i] + dp[stack[-1][1]]

        res += dp[i]
        stack.append((value_list[i], i))

    return 2 * res / ((n + 1) * n)


print(solve())
