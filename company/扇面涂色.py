# coding = utf-8

# 扇面涂色，相邻不同色

n, m = map(int, input().split())


def backtrack(n, m):
    if n == 1:
        return m
    if n == 2:
        if m < 2:
            return 0
        else:
            return m * (m - 1)

    return m * (m - 1)**(n - 1) - backtrack(n - 1, m)


print(backtrack(n, m))
