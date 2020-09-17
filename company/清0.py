# coding = utf-8

# 给定一个 0, 1字符串，翻转第i个字符，则相邻的也要翻转。判断最后是否可以全为0.


def flip(s, i):
    def __flip(s, i):
        s = s[:i] + str(1 - int(s[i])) + s[i + 1:]
        return s

    s = __flip(s, i - 1)
    s = __flip(s, i)
    if i < len(s) - 1:
        s = __flip(s, i + 1)
    return s


def judge(s: str):
    cnt = 0
    n = len(s)
    for i in range(n - 1):
        if s[i] == '1':
            s = flip(s, i + 1)
            cnt += 1

    return cnt if s[n - 1] == '0' else -1


def solve():
    N = int(input())
    for _ in range(N):
        s = input()
        res = judge(s)
        if res == -1:
            print('No')
        else:
            print(res)
    return


solve()