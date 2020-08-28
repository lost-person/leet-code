# coding = utf-8

N = int(input())

def judge(l1, l2):
    set_list = []
    for i in range(0, 6, 2):
        set_list.append(sum(l1[i:i+2]))
    
    for i in range(0, 6, 2):
        flag = False
        for j in range(3):
            if sum(l2[i: i + 2]) == set_list[j]:
                flag = True
                break
        if not flag: return False
    return True

data = []
cls_list = list(range(N))

for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(N - 1):
    for j in range(i + 1, N):
        if cls_list[j] != j: continue
        else:
            if judge(data[i], data[j]): cls_list[j] = i

cls_dict = dict()
for cls_ in cls_list:
    cls_dict[str(cls_)] = cls_dict.get(str(cls_), 0) + 1

num_cls = len(cls_dict)
cls_dict = dict(sorted(cls_dict.items(), key=lambda kv: (kv[1], int(kv[0]))))
cls_str = []
for k, v in cls_dict.items():
    cls_str.append(str(v))

print(num_cls)
print(' '.join(cls_str))
