# coding = utf-8

N, M, T = map(int, input().split())

if T == 0: 
    res = 0
else:
    # 午餐
    lanuch_list = []
    for i in range(N):
        lanuch_list.append(list(map(int, input().split())))
    
    # 晚餐
    dinner_list = []
    for i in range(M):
        dinner_list.append(list(map(int, input().split())))
    
    lanuch_list = list(sorted(lanuch_list, key=lambda x: x[0] / x[1]))
    dinner_list = list(sorted(dinner_list, key=lambda x: x[0] / x[1]))

    if lanuch_list[0][1] + dinner_list[0][1] < T:
        res = -1
    elif lanuch_list[0][1] >= T and dinner_list[0][1] >= T:
        res = min(lanuch_list[0][1], dinner_list[0][1])
    elif lanuch_list[0][1] >= T:
        res = lanuch_list[0][1]
    elif dinner_list[0][1] >= T:
        res = dinner_list[0]
    elif lanuch_list[0][1] + dinner_list[0][1] >= T:
        res = lanuch_list[0][1] + dinner_list[0][1]
    else:
        i, j = 0, 0
        flag = False
        while i < N and j < M:
            lanuch = lanuch_list[i][1]
            dinner = dinner_list[j][1]
            if lanuch + dinner >= T:
                res = lanuch + dinner
                flag = True
                break
            else:
                if (lanuch_list[i][1] / lanuch_list[i][0]) > (dinner_list[j][1] / lanuch_list[j][0]):
                    i += 1
                else:
                    j += 1
        if not flag:
            res = -1
print(res)
