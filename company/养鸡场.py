# coding = utf-8

# N个养鸡场，每个鸡场有Ni只鸡，每天每个鸡场增加K只鸡，
# 每天结束时卖掉鸡最多的那个场的所有鸡的一半，求M天后剩余鸡总数

import heapq as hp

def solve():
    N, M, K = map(int, input().split())
    chicken_list = list(map(int, input().split()))
    chicken_list = list(map(lambda x: -x, chicken_list))
    hp.heapify(chicken_list)
    for i in range(M):
        tmp = -hp.heappop(chicken_list) - (i + 1) * K
        tmp = tmp // 2
        hp.heappush(chicken_list, -tmp)
    
    res = 0
    for i in range(N):
        res += -hp.heappop(chicken_list)
    return res + N * M * K

print(solve())
