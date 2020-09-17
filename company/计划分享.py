# coding = utf-8


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    step = 0
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i, num in enumerate(nums):
        dp[i + 1][num] = True

    for row in range(1, n + 1):
        if dp[row][row]:
            return step

    while True:
        step += 1
        for row in range(1, n + 1):
            if dp[row][row]:
                return step

        prev_dp = dp[:][:]
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        for col in range(1, n + 1):
            for row in range(1, n + 1):
                if prev_dp[row][col]:
                    dp[row][nums[col - 1]] = True


def solve2():
    n = int(input())
    nums = list(map(int, input().split()))

    dp = [set() for i in range(n + 1)]
    for i, num in enumerate(nums):
        dp[num].add(i + 1)

    for i in range(1, n + 1):
        if i in dp[i]:
            return 0

    step = 1
    while True:
        step += 1

        prev_dp = dp[:]
        dp = [set() for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[nums[i - 1]] |= prev_dp[i]

        for i in range(1, n + 1):
            if i in dp[i]:
                return step


print(solve2())
