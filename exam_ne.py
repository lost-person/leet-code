# coding = utf-8


def solve(data):
    if len(data) != len(set(data)): return "NO"
    else:
        b, w, t = [0] * 15, [0] * 15, [0] * 15
        num_set = set()

        # 对号入座
        for d in data:
            if d[1] == 'B':
                b[int(d[0])] = 1
            elif d[1] == 'W':
                w[int(d[0])] = 1
            else:
                t[int(d[0])] = 1
            num_set.add(int(d[0]))
        
        bb, ww, tt = -1, -2, -3
        # 判断 1, 2, 3
        for i in range(1, 8, 3):
            if b[i] == 1: bb = 1
            elif w[i] == 1: ww = 1
            elif t[i] == 1: tt = 1
        
        if bb == ww or bb == tt or ww == tt:
            return "NO"
        
        for i in range(2, 9, 3):
            if b[i] == 1: bb = 2
            elif w[i] == 1: ww = 2
            elif t[i] == 1: tt = 2
        
        if bb == ww or bb == tt or ww == tt:
            return "NO"
        
        for i in range(3, 10, 3):
            if b[i] == 1: bb = 3
            elif w[i] == 1: ww = 3
            elif t[i] == 1: tt = 3
        
        if bb == ww or bb == tt or ww == tt:
            return "NO"
        
        if bb + tt + ww == 6:
            return "YES"
        else:
            return "NO"

T = int(input())

i = 0
while i < T:
    data = input().split()
    print(solve(data))
    i += 1