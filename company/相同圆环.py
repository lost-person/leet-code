# coding = utf-8

import sys

def solve():
    T = int(input())
    while T > 0:
        T -= 1
        n = int(input())
        my_set = set()
        circles = []

        res = "NO"
        for i in range(n):
            nums = list(map(int, input().split()))
            nums.sort()
            ss = ""
            for j in range(6):
                ss += str(nums[j])
                ss += "#"
            if ss in my_set:
                res = "YES"
            my_set.add(ss)
        
        print(res)

solve()
