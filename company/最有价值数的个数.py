# coding = utf-8

# 对一个数组，求每个数左边比他大的数的最小值，右边比他小的数的最大值，若这两个数成倍数关系，记录。

import bisect

num = list(map(int, input().split()))
n = len(num)

left_max = [float('-inf')] * n
right_min = [float('inf')] * n
left, right = [], []

for i in range(n):
    if left:
        index = bisect.bisect(left, -num[i])
        if index != 0:
            left_max[i] = -left[index - 1]
    bisect.insort(left, -num[i])

for i in range(n - 1, -1, -1):
    if right:
        index = bisect.bisect(right, num[i])
        if index != 0:
            right_min[i] = right[index - 1]
    bisect.insort(right, num[i])

res = 0
for i in range(n):
    if left_max[i] > float('-inf') and right_min[i] < float('inf') and  left_max[i] % right_min[i] == 0:
        res += 1

print(res)