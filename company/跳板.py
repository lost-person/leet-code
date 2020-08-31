# coding = utf-8

# N 跳板，最多跳 k 次，可获取跳板与当前高度差最多为H, 借助跳板跳跃高度为对称，求最高高度。
from collections import deque

N, K, H = map(int, input().split())
h_list = [int(input()) for _ in range(N)]

queue = deque()
queue.appendleft((K, 0, 0)) # jump_cnt, cur_hight, jump
h_max = 0

while queue:
    jump_cnt, cur_hight, jump = queue.pop()
    next_hight = jump * 2 - cur_hight
    if next_hight > h_max:
        h_max = next_hight
    for i in range(N):
        if next_hight + H >= h_list[i] > next_hight:
            if jump_cnt >= 1:
                queue.appendleft((jump_cnt - 1, next_hight, h_list[i]))
print(h_max)