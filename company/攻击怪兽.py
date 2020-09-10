# coding = utf-8

import heapq as hp

# N 怪兽，M 支箭。每个怪兽都有血量，每只弓箭都有攻击力和价值，求消灭怪兽的最小价值和。弓箭攻击不能叠加。

def min_value():
    N, M = map(int, input().split())
    if M < N:
        return -1

    monst_list = list(map(int, input().split())) # N
    monst_list.sort(key=lambda x: -x)

    value_list = list(map(int, input().split())) # M
    attack_list = list(map(int, input().split())) # M
    arrow_list = [(value, attack) for value, attack in zip(value_list, attack_list)] # M
    arrow_list.sort(key=lambda x: -x[1])

    del attack_list
    value_list = []
    
    res = 0
    j = 0
    for i in range(N):
        while j < M and arrow_list[j][1] >= monst_list[i]:
            hp.heappush(value_list, - arrow_list[j][0])
            j += 1
        if not value_list:
            return -1
        else:
            res += -value_list.pop()
    
    return res

print(min_value())
