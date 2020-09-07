# coding = utf-8

import sys
import math

def solve():
    L, d = map(int, input().split())
    if L <= d:
        print("0.0000")
    else:
        print("%.4f"%(1 + math.log(L / d)))

solve()
