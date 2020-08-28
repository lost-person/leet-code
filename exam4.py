# coding = utf-8

res = ''

data = []
for i in range(6):
    data.append(list(input()))

num = 0
coor_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _data in data:
    for _d in data:
        if _d != '#': num += 1

food_list = list(range(6))

def dfs(x, y, food_id):
    # 抵达终点
    if num == 0: return True
    for coor in coor_list:
        new_x = x + coor
        new_y = y + coor
        if 0 <= new_x < 6 and 0 <= new_y < 6 and data[new_x][new_y] != '#':
            num -= 1
            
            for food_id_ in food_id:
                if food_id_ != food_id: 
                    if dfs(new_x, new_y, food_id): 
    return False

for i in range(data):
