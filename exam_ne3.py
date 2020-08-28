# coding = utf-8

def solve(N):
    de = 0
    index = 0
    all_time = 0
    self_time = 0
    dep = [0] * N
    dep_list = []
    A = []
    
    max_time = 0
    res_id = 0
    
    for i in range(N):
        cur_input = input().split()
        begin_time = int(cur_input[0])
        idx = int(cur_input[1])
        flag = int(cur_input[2])
        if flag == 0:
            de += 1
            dep[de] = 0
        else:
            de -= 1
        A.append([begin_time, idx, de])

        if flag == 0:
            dep_list.append(i)
        else:
            index = dep_list.pop()
            all_time = A[i][0] - A[index][0]
            dep[A[index][2] - 1] += all_time
            self_time = all_time - dep[A[index][2]]
            dep[A[index][2]] = 0
            
            # 选出最大的
            if self_time > max_time:
                max_time = self_time
                res_id = A[i][1]
            
            if self_time == max_time:
                res_id = min(res_id, A[i][1])
 
    return res_id

T = int(input())

i = 0
while i < T:
    N = int(input())
    print(solve(N))
    i += 1