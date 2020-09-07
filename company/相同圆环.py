# coding = utf-8

import sys

def judge(circles, index_list, index1, index2):
    if sum(circles[index1]) != sum(circles[index2]):
        return False

    return sum(map(lambda x, y: x - y, index_list[index1], index_list[index2])) == 0
    

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
