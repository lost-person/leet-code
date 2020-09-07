# coding = utf-8

# 动物投票。每个动物只会投票给自己崇拜的动物或者自身，求每位动物最高的票数。（A_i <= i）

def solve():
    n = int(input())
    ans = [0] * (n + 1)
    animal_list = [-1] + list(map(int, input().split()))

    for i in range(n, 0, -1):
        ans[i] += 1
        ans[animal_list[i]] += ans[i]

    for i in range(1, n + 1):
        print(ans[i])
solve()
