# coding = utf-8

# 网格染色，相邻不同色，染料总数和方格总数相同

T = int(input())

for i in range(T):
    n, m, c = map(int, input().split())
    color_list = list(map(int, input().split()))
    visisted = [[-1] * m for _ in range(n)] # 记录

    res = (n * m + 1) // 2
    flag = True
    for color in color_list:
        if color > res:
            flag = False
            break
    
    if flag:
        print('YES')
    else:
        print('NO')
