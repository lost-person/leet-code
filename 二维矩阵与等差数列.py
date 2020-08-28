# coding = utf-8

def solve():
    n, m, q = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    query_list = [list(map(int, input().split())) for _ in range(q)]

print(solve())