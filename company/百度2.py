# coding = utf-8

def solve():
    n, m = map(int, input().split())

    i = 0
    cmp_res = []
    while i < m:
        a, b = map(int, input().split())
        cmp_res.append([a - 1, b - 1])
        i += 1

    # 拓扑排序 bfs
    in_degree = [0] * n
    adj_matrix = [[] for _ in range(n)]

    for a, b in cmp_res:
        in_degree[b] += 1
        adj_matrix[a].append(b)

    queue = []
    for i in range(n):
        if not in_degree[i]:
            queue.append(i)
    
    res = []
    max_num, min_num = -1, -1
    if len(queue) == 1:
        max_num = queue[0]

    while queue:
        a = queue.pop()
        min_num = a
        n -= 1
        for b in adj_matrix[a]:
            in_degree[b] -= 1
            if not in_degree[b]:
                queue.append(b)

    if n != 0:
        min_num = -1

    res = []
    if max_num != -1:
        res.append(str(max_num + 1))
    else:
        res.append("-1")
    
    if min_num != -1:
        res.append(str(min_num + 1))
    else:
        res.append("-1")

    return " ".join(res)

print(solve())
