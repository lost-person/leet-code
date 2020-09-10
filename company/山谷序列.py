# coding = utf-8

import sys

def solve():
    T = int(input())
    while T > 0:
        T -= 1
        
        n = int(input())
        nums = list(map(int, input().split()))
        nums = [int(num) for num in nums]
        
        dpl = [1] * n
        dpr = [1] * n
        res = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] < nums[j]:
                    dpl[i] = max(dpl[i], dpl[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] < nums[j]:
                    dpr[i] = max(dpr[i], dpr[j] + 1)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    res = max(res, 2 * min(dpl[i], dpr[j]))
        
        print(res)

solve()
