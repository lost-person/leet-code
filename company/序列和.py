# coding = utf-8

# 长度不小于L的和为N的最短序列

N, L = map(int, input().split())

if L > 100:
    print("No")

is_found = False
start = 0

for l in range(L, 102):
    if (2 * N - l * l + l) % (2 * l) == 0:
        start = (2 * N + l - l**2) // (2 * l)
        ans = [str(i) for i in range(start, start + l)]
        print(' '.join(ans))
        break

if l > 100:
    print("No")
